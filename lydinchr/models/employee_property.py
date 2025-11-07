from odoo import models, fields, api


class EmployeeProperty(models.Model):
    _name = 'employee.property'
    _description = 'Employee Property'
    _order = 'date desc, id desc'

    name = fields.Char(string='Property Name', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, ondelete='cascade')
    category = fields.Selection([
        ('equipment', 'Equipment'),
        ('document', 'Document'),
        ('asset', 'Asset'),
        ('credential', 'Credential'),
        ('other', 'Other')
    ], string='Category', required=True, default='equipment')
    value = fields.Char(string='Value/Description')
    date = fields.Date(string='Assignment Date', default=fields.Date.context_today, required=True)
    return_date = fields.Date(string='Return Date')
    status = fields.Selection([
        ('assigned', 'Assigned'),
        ('returned', 'Returned'),
        ('lost', 'Lost'),
        ('damaged', 'Damaged')
    ], string='Status', default='assigned', required=True)
    notes = fields.Text(string='Notes')
    active = fields.Boolean(string='Active', default=True)

    @api.depends('name', 'category')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"[{dict(record._fields['category'].selection).get(record.category)}] {record.name}"

