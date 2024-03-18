from odoo import api, fields, models, _


class Vehicle(models.Model):

    _name = 'delivery.vehicle'
    _description = 'Vehicle Information'


    name = fields.Char(string='Brand', required=True)
    model = fields.Char(string='Model', required=True)
    license_plate = fields.Char(string='License Plate')


