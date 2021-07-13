from odoo import fields, models, api


class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"
    # TAB SCONTO DETRAZIONE
    testo_sconto_detrazione = fields.Html('Testo sconto detrazione')


