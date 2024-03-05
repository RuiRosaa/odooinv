from odoo import models, fields, api


class Carrinha(models.Model):
    _name = 'odooinv.carrinha'
    _description = 'Modelo para Carrinhas'

    name = fields.Char(string='Nome', required=True)
    model = fields.Char(string='Modelo')
    type = fields.Selection([('empresa', 'Empresa'), ('alugada', 'Alugada')], string='Tipo', default='empresa')
    capacity = fields.Float(string='Capacidade de Carga')
