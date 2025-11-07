from odoo import models, fields, api


class HRLeaveExtended(models.Model):
    _inherit = 'hr.leave'

    # Additional leave tracking fields
    leave_reason = fields.Text(string='Leave Reason', help='Detailed reason for the leave')
    contact_during_leave = fields.Char(string='Contact Number During Leave')
    address_during_leave = fields.Text(string='Address During Leave')
    backup_employee_id = fields.Many2one('hr.employee', string='Backup Employee', 
                                         help='Employee covering during leave')
    is_emergency = fields.Boolean(string='Emergency Leave', default=False)
    
    # Approval tracking
    approved_by_id = fields.Many2one('res.users', string='Approved By', readonly=True)
    approved_date = fields.Datetime(string='Approval Date', readonly=True)
    rejection_reason = fields.Text(string='Rejection Reason')
    
    def action_approve(self):
        res = super(HRLeaveExtended, self).action_approve()
        for leave in self:
            leave.write({
                'approved_by_id': self.env.user.id,
                'approved_date': fields.Datetime.now()
            })
        return res

