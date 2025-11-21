# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class TaskAssignment(models.Model):
    _name = 'task.assignment'
    _description = 'Task Assignment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'priority desc, deadline asc, id desc'

    name = fields.Char(string='Task Title', required=True, tracking=True)
    description = fields.Text(string='Description', tracking=True)
    assigner_id = fields.Many2one(
        'res.users', string='Assigner', default=lambda self: self.env.user, tracking=True,
        help='Người giao việc. Mặc định là người tạo task.')
    assignee_ids = fields.Many2many(
        'res.users', 'task_assignment_user_rel', 'task_id', 'user_id', string='Assignees',
        tracking=True, help='Danh sách người được giao task. Có thể bao gồm cả người giao.')

    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Urgent'),
    ], string='Priority', default='1', tracking=True)

    state = fields.Selection([
        ('draft', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)

    start_date = fields.Datetime(string='Start Date', tracking=True)
    deadline = fields.Datetime(string='Deadline', tracking=True)
    completion_date = fields.Datetime(string='Completion Date', readonly=True)

    tag_ids = fields.Many2many('hr.skill', string='Tags', help='Nhãn hoặc kỹ năng liên quan đến task.', tracking=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

    # computed helpers
    assignee_count = fields.Integer(string='Assignees', compute='_compute_assignee_count', store=False)

    @api.depends('assignee_ids')
    def _compute_assignee_count(self):
        for task in self:
            task.assignee_count = len(task.assignee_ids)

    @api.constrains('assignee_ids')
    def _check_assignees_not_empty(self):
        for task in self:
            if not task.assignee_ids:
                raise ValidationError(_('Task phải có ít nhất một người nhận.'))

    def action_start(self):
        self.write({'state': 'in_progress'})
        return True

    def action_done(self):
        self.write({'state': 'done', 'completion_date': fields.Datetime.now()})
        return True

    def action_cancel(self):
        self.write({'state': 'cancelled'})
        return True

    def action_reset(self):
        self.write({'state': 'draft', 'completion_date': False})
        return True

    @api.model
    def create(self, vals):
        task = super().create(vals)
        if task.assignee_ids:
            for user in task.assignee_ids:
                task.activity_schedule(
                    'mail.mail_activity_data_todo',
                    note=_('Bạn được giao task: %s') % task.name,
                    user_id=user.id,
                )
        return task
