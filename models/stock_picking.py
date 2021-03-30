from odoo import api, fields, models, _


class stock_picking_template(models.Model):
    _inherit = "stock.picking"

    codice_tracking_spedizione = fields.Char('Codice tracking spedizione')