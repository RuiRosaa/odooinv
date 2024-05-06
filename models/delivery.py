from ast import literal_eval
import time
from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, format_datetime, format_date, groupby


class DeliveryTeam(models.Model):
    _name = 'delivery.team'
    _description = 'Delivery Team'

    name = fields.Char('Delivery Teams')
    driver_id = fields.Many2one('delivery.driver', string='Driver', required=True)
    vehicle_id = fields.Many2one('delivery.vehicle', string='Vehicle', required=True)
    route = fields.Many2one('delivery.route', string='Route', required='False')
    location = fields.Char('Location')
    count_picking_late = fields.Integer(compute='_compute_picking_count')
    count_picking_in_progress = fields.Integer(compute='_compute_picking_count')

    def _compute_picking_count(self):
        domains = {
            'count_picking_late': [('scheduled_date', '<', time.strftime(DEFAULT_SERVER_DATETIME_FORMAT)),
                                   ('state', 'in', ('assigned', 'waiting', 'confirmed'))],
            'count_picking_in_progress': [('scheduled_date', '<', time.strftime(DEFAULT_SERVER_DATETIME_FORMAT)),
                                   ('state', 'in', ('assigned', 'waiting', 'confirmed'))]
        }
        for field_name, domain in domains.items():
            data = self.env['stock.picking']._read_group(domain +
                [('state', 'not in', ('done', 'cancel')), ('picking_type_id', 'in', self.ids)],
                ['picking_type_id'], ['__count'])
            count = {picking_type.id: count for picking_type, count in data}
            for record in self:
                record[field_name] = count.get(record.id, 0)

    def _get_action(self, action_xmlid):
        action = self.env["ir.actions.actions"]._for_xml_id(action_xmlid)
        if self:
            action['display_name'] = self.display_name

        context = {
            'search_default_picking_type_id': [self.id],
            'default_picking_type_id': self.id,
            #'default_company_id': self.company_id.id,
        }

        action_context = literal_eval(action['context'])
        context = {**action_context, **context}
        action['context'] = context
        return action

    def get_action_picking_tree_late(self):
        return self._get_action('stock.action_picking_tree_late')

    @api.model
    def create(self, vals):
        team = super(DeliveryTeam, self).create(vals)
        if team.driver_id:
            team.driver_id.write({'status': 'inactive'})
        return team

    def write(self, vals):
        res = super(DeliveryTeam, self).write(vals)
        if 'driver_id' in vals:
            driver_id = vals.get('driver_id')
            if driver_id:
                self.driver_id.write({'status': 'inactive'})
        return res

    def unlink(self):
        for team in self:
            if team.driver_id:
                team.driver_id.sudo().write({'status': 'active'})
        return super(DeliveryTeam, self).unlink()

    @api.onchange('driver_id')
    def _onchange_driver_id(self):
        if self.driver_id:
            self.driver_id.write({'status': 'inactive'})


class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    city = fields.Char(string='City')

    delivery_team_id = fields.Many2one('delivery.team', string='Delivery Team', help='Select the delivery team')
    customer_city = fields.Char(string='Partner City', related='picking_ids.partner_id.city', readonly=True)
    delivery_team_name = fields.Char(string="Team Name")


class CustomerCityDeliveries(models.Model):
    _inherit = 'stock.picking'

    partner_city = fields.Char(string='Partner City', related='partner_id.city', readonly=True)
