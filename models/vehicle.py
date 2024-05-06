from odoo import api, fields, models, _


class Vehicle(models.Model):

    _name = 'delivery.vehicle'
    _description = 'Vehicle Information'

    name = fields.Char(string='Brand', required=True)
    model = fields.Char(string='Model', required=True)
    license_plate = fields.Char(string='License Plate')
    km = fields.Char(string='Kilometers')
    insurance = fields.Char(string='Insurance', required=True)
    endinsurance = fields.Date(string='Insurance Validity')

    max_weight = fields.Float(string='Max Weight (kg)', required=True)
    max_space = fields.Integer(string='Max Space (m^3)', required=True)

