{
	'name': 'HR Multi-Org',
	'category': 'Human Resources',
	'version': '19.0.1.0.0',
	'summary': 'Multi-manager, multi-position employees and organization structure',
	'author': 'You',
	'license': 'LGPL-3',
	'depends': ['hr', 'hr_org_chart'],
	'data': [
		'security/ir.model.access.csv',
		'views/hr_employee_views.xml',
	],
	'installable': True,
	'application': True,
}
