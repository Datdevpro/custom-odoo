{
    'name': 'Lydinc HR Custom',
    'version': '19.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Custom HR module for employee management, properties, and leave tracking',
    'description': """
        Lydinc HR Custom Module
        =======================
        
        This module extends Odoo's HR functionality with:
        * Extended employee information (salary, emergency contacts, badge numbers)
        * Employee property tracking (equipment, documents, assets)
        * Enhanced leave management with additional workflow fields
        
        Features:
        ---------
        * Track employee salary components (basic, housing, transport, other allowances)
        * Manage employee properties and assignments
        * Enhanced leave request with emergency contacts and backup employees
        * Custom security groups and access rights
    """,
    'author': 'Lee',
    'website': 'https://www.lydinc.com',
    'depends': [
        'base',
        'hr',
        'hr_holidays',
    ],
    'data': [
        # Security
        'security/lydinchr_security.xml',
        'security/ir.model.access.csv',
        
        # Data
        'data/employee_property_data.xml',
        
        # Views
        'views/hr_employee_views.xml',
        'views/employee_property_views.xml',
        'views/hr_leave_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
