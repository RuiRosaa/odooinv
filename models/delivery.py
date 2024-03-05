from odoo import api, fields, models, _


class DeliveryTeam(models.Model):
    _inherit = 'stock.picking'
    _name = 'delivery.team'
    _description = 'Delivery Team'

    name = fields.Char(string='Batch Transfer')


class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    delivery_team_id = fields.Many2one('delivery.team', string='Delivery Team', help='Select the delivery team')


#class StockPicking(models.Model):
     #_inherit = 'stock.picking.batch'

    #name = fields.Char(string='Delivery Team')
    #delivery_team = fields.Many2one('delivery.team', string='Delivery Team', ondelete={'cascade': 'set null'})


