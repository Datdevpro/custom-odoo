# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CustomHREmployee(models.Model):
    _inherit = 'hr.employee'

    # Trường cho phép nhiều người quản lý
    manager_ids = fields.Many2many(
        'hr.employee',
        'hr_employee_custom_manager_rel',
        'employee_id',
        'manager_id',
        string='Managers',
        help='Danh sách các người quản lý của nhân viên này. Có thể có nhiều người quản lý.',
        domain="[('id', '!=', id)]"  # Không cho phép tự quản lý
    )

    # Trường tính toán để hiển thị tổng số người quản lý
    manager_count = fields.Integer(
        string='Number of Managers',
        compute='_compute_manager_count',
        store=False
    )

    @api.depends('manager_ids', 'parent_id')
    def _compute_manager_count(self):
        """Tính tổng số người quản lý (bao gồm parent_id và manager_ids)"""
        for employee in self:
            count = len(employee.manager_ids)
            if employee.parent_id:
                count += 1
            employee.manager_count = count

    @api.constrains('manager_ids', 'parent_id')
    def _check_manager_not_self(self):
        """Đảm bảo nhân viên không thể tự quản lý"""
        for employee in self:
            if employee.parent_id == employee:
                raise models.ValidationError("Nhân viên không thể tự quản lý chính mình.")
            if employee in employee.manager_ids:
                raise models.ValidationError("Nhân viên không thể tự quản lý chính mình.")

