{
    'name': 'Custom Employees - Multi Managers',
    'version': '19.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Mở rộng module Employees để hỗ trợ nhiều người quản lý cho một nhân viên',
    'description': """
Custom Employees Module
======================

Module này mở rộng chức năng của module Employees gốc với các tính năng:

* Hỗ trợ nhiều người quản lý: Một nhân viên có thể được quản lý bởi nhiều người
* Layout giống hệt module Employees gốc
* Hiển thị số lượng người quản lý trong danh sách
* Tìm kiếm và lọc theo người quản lý

Tính năng:
----------
* Thêm trường "Additional Managers" trong form nhân viên
* Hiển thị tổng số người quản lý (bao gồm Manager chính và Additional Managers)
* Tìm kiếm nhân viên theo người quản lý
* Giao diện giống hệt module Employees gốc
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': [
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}

