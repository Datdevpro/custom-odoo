from odoo import api, fields, models


class HREmployeeMultiOrg(models.Model):
	_inherit = 'hr.employee'

	# Multi managers: a primary one (mirrors hr.employee.parent_id) + additional managers
	manager_ids = fields.Many2many(
		comodel_name='hr.employee',
		relation='hr_employee_manager_rel',
		column1='employee_id', column2='manager_id',
		string='Additional Managers',
		help='Employees who also manage this employee besides the primary manager.')

	primary_manager_id = fields.Many2one(
		'hr.employee', string='Primary Manager',
		compute='_compute_primary_manager', inverse='_inverse_primary_manager', store=True)

	# Multi positions and departments
	position_ids = fields.Many2many(
		'hr.job', 'hr_employee_job_rel', 'employee_id', 'job_id', string='Positions')
	department_ids = fields.Many2many(
		'hr.department', 'hr_employee_department_rel', 'employee_id', 'department_id', string='Departments')

	@api.depends('parent_id')
	def _compute_primary_manager(self):
		for emp in self:
			emp.primary_manager_id = emp.parent_id

	def _inverse_primary_manager(self):
		for emp in self:
			emp.parent_id = emp.primary_manager_id

	def action_open_org_chart(self):
		# convenience action: open org chart on this employee if hr_org_chart installed
		return {
			'type': 'ir.actions.client',
			'tag': 'hr_org_chart',
			'params': {
				'employee_id': self.id,
			},
		}
