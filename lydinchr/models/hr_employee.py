from odoo import models, fields, api


class HREmployeeExtended(models.Model):
    _inherit = 'hr.employee'

    # Employee identification
    employee_badge_number = fields.Char(string='Badge Number', help='Employee badge or ID number')
    joining_date = fields.Date(string='Joining Date', help='Date when employee joined the company')
    
    # Salary information
    basic_salary = fields.Monetary(string='Basic Salary', currency_field='currency_id')
    housing_allowance = fields.Monetary(string='Housing Allowance', currency_field='currency_id')
    transport_allowance = fields.Monetary(string='Transport Allowance', currency_field='currency_id')
    other_allowance = fields.Monetary(string='Other Allowance', currency_field='currency_id')
    total_salary = fields.Monetary(string='Total Salary', compute='_compute_total_salary', store=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    
    # Emergency contact
    emergency_contact_name = fields.Char(string='Emergency Contact Name')
    emergency_contact_relationship = fields.Char(string='Relationship')
    emergency_contact_phone = fields.Char(string='Emergency Phone')
    emergency_contact_address = fields.Text(string='Emergency Contact Address')
    
    # Properties
    property_ids = fields.One2many('employee.property', 'employee_id', string='Properties')
    property_count = fields.Integer(string='Property Count', compute='_compute_property_count')
    
    @api.depends('basic_salary', 'housing_allowance', 'transport_allowance', 'other_allowance')
    def _compute_total_salary(self):
        for employee in self:
            employee.total_salary = (
                (employee.basic_salary or 0) +
                (employee.housing_allowance or 0) +
                (employee.transport_allowance or 0) +
                (employee.other_allowance or 0)
            )
    
    @api.depends('property_ids')
    def _compute_property_count(self):
        for employee in self:
            employee.property_count = len(employee.property_ids.filtered(lambda p: p.status == 'assigned'))

