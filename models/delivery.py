from odoo import api, fields, models, _


class DeliveryTeam(models.Model):

    _name = 'delivery.team'
    _description = 'Delivery Team'

    name = fields.Char('Delivery Teams')
    driver_id = fields.Many2one('delivery.driver', string='Driver', required=True)
    vehicle_id = fields.Many2one('delivery.vehicle', string='Vehicle', required=True)


class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    city = fields.Char(string='City')

    delivery_team_id = fields.Many2one('delivery.team', string='Delivery Team', help='Select the delivery team')
    customer_city = fields.Char(string="Costumer City")
    delivery_team_name = fields.Char(string="Team Name")
