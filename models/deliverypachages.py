from odoo import api, fields, models, _


class DeliveryPackages(models.Model):
    _name = 'delivery.vehicle'
    _description = 'Vehicle Information'

    name = fields.Char(string='Package', required=True)
    package_volume = fields.Integer(string='Package Volume', required=True)
    package_weight = fields.Float(string='Package Weight (kg)', required=True)
