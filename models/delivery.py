from odoo import api, fields, models, _


class DeliveryTeam(models.Model):
    _name = 'delivery.team'
    _description = 'Delivery Team'

    name = fields.Char(string='Team Name')



class StockPicking(models.Model):
    _inherit = 'stock.picking'

   # delivery_team = fields.Many2one('delivery.team', string='Delivery Team', ondelete={'cascade': 'set null'})
