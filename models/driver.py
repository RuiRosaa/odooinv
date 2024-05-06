from odoo import api, fields, models, _


class Driver(models.Model):
    _name = 'delivery.driver'
    _description = 'Driver Information'

    name = fields.Char(string='Name', required=True)
    status = fields.Selection([
        ('active', 'Available'),
        ('inactive', 'Unavailable')
    ], string='Status', default='active')
    driverlicensetype = fields.Char(string='License Type', required=True)
    licensevalidity = fields.Date(string='License Validity')
