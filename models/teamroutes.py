from odoo import models, fields, api


class TeamRoutes(models.Model):
    _name = 'delivery.route'
    _description = 'Route'

    name = fields.Char(string='Route Name')
    city = fields.Char(string='Cities')
