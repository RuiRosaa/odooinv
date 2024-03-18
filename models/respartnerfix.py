from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    property_payment_method_id = fields.Many2one('payment.method', string='Payment Method')
