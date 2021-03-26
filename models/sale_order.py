from odoo import api, fields, models, _


class sale_order_template(models.Model):
    _inherit = "sale.order"

    testo_sconto_detrazione = fields.Text('Testo sconto detrazione')