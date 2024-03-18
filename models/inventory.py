from odoo import api, fields, models, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    _name = 'stock.pickingodoo'
    _description = 'Inventory Deliveries'

    customer_city = fields.Char(string='Customer City')
