{
    'name': 'GearGuard: Maintenance Tracker',
    'version': '1.0',
    'category': 'Maintenance',
    'summary': 'Track assets and manage maintenance requests',
    'description': 'A comprehensive maintenance management system for tracking equipment and handling maintenance requests.',
    'author': 'Your Name',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/equipment_views.xml',
        'views/maintenance_team_views.xml',
        'views/maintenance_request_views.xml',
        'views/menu.xml',
        'data/demo.xml',
    ],
    'installable': True,
    'application': True,
}