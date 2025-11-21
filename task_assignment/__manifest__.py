{
    'name': 'Task Assignment',
    'version': '19.0.1.0.0',
    'summary': 'Assign tasks to employees with multiple assignees and workflow controls',
    'description': """
Task Assignment
===============

Module custom cho phép giao việc nội bộ với các tính năng:
- Bất kỳ người dùng nội bộ nào cũng có thể giao task
- Giao một task cho nhiều người nhận
- Theo dõi trạng thái, ưu tiên và deadline
- Tích hợp chatter/activity để thông báo
""",
    'category': 'Productivity',
    'author': 'Your Company',
    'depends': ['base', 'hr', 'mail'],
    'data': [
        'security/task_assignment_security.xml',
        'security/ir.model.access.csv',
        'views/task_assignment_views.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
