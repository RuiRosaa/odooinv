{
    'name': 'Delivery Team Management',
    'version': '1.1',
    'category': 'Generic',
    'author': 'Rui Pedro',
    'depends': ['sale','base','stock','stock_picking_batch'],
    'description': """
        Odoo Module for Internship Project
        ===============================================
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/delivery.xml',
        'views/menu.xml',
        'views/teams.xml',
        'views/inventory.xml',
        'views/drivers.xml',
        'views/vehicles.xml',
        'views/routes.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'license': 'LGPL-3'
}
