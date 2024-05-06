from odoo import api, fields, models, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    _name = 'stock.pickingodoo'
    _description = 'Inventory Deliveries'

    customer_city = fields.Char(string='Customer City')


class Inventory(models.Model):
    _inherit = 'stock.picking'

    delivery_team_id = fields.Many2one('delivery.team', string='Delivery Team')
