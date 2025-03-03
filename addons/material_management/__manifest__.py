{
    'name': 'Material Management',
    'version': '1.0',
    'summary': 'Manage materials and suppliers',
    'description': 'A module to manage materials and their related suppliers.',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'category': 'Inventory',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/material_views.xml',
        'views/supplier_views.xml',
    ],
    'installable': True,
    'application': True,
}