{
    'name': 'Delivery Team Management',
    'author': 'Rui Pedro',
    'summary': 'Odoo 17 Delivery Team',
    'depends': ['sale','base','stock','stock_picking_batch'],
    'data': [
        'security/ir.model.access.csv',
        'views/delivery.xml',
        'views/menu.xml',
        'views/teams.xml',
        'views/inventory.xml',
        'views/drivers.xml',
        'views/vehicles.xml'
    ]
}
