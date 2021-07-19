from datetime import datetime, timedelta
from odoo import SUPERUSER_ID
from odoo import api, fields, models, _
from odoo.http import request


class product_template(models.Model):
	_inherit = "product.template"

	# TAB F-GAS
	tipologia_gas_sel = fields.Many2one('golemme.tipologia_gas_sel', string="Tipologia gas")
	qta_gas_precaricato = fields.Float('Q.tà gas precaricato', digits=(8,2))

	# TAB CARATTERISTICHE
	marca = fields.Many2one('golemme.marca', string="Marca")
	modello = fields.Many2one('golemme.modello', string="Modello")
	tipologia = fields.Many2one('golemme.tipologia', string="Tipologia")
	alimentazione = fields.Many2one('golemme.alimentazione', string="Alimentazione")
	classe = fields.Many2one('golemme.classe', string="Classe energetica")
	telecomando = fields.Many2one('golemme.telecomando', string="Telecomando")
	tecnologia = fields.Many2one('golemme.tecnologia', string="Tecnologia")
	unita = fields.Many2one('golemme.unita', string="Unita")
	wifi = fields.Many2one('golemme.wifi', string="Wi-Fi")
	garanzia = fields.Many2one('golemme.garanzia', string="Garanzia")
	colore = fields.Many2one('golemme.colore', string="Colore")
	tipologia_installazione = fields.Many2one('golemme.tipologia_installazione', string="Tipologia installaz.")
	detrazione_fiscale = fields.Boolean(string="Detrazione fiscale")
	capacita_raffreddamento = fields.Char('Cap. raffreddamento')
	capacita_riscaldamento = fields.Char('Cap. riscaldamento')
	rumorosita = fields.Char('Rumorosità')
	kw = fields.Float('KW', digits=(8,2))
	altezza = fields.Float('Altezza', digits=(8,2))
	lunghezza = fields.Float('Lunghezza', digits=(8,2))
	larghezza = fields.Float('Larghezza', digits=(8,2))
	peso = fields.Float('Peso', digits=(8,2))
	link_schede_tecniche = fields.Html('Link schede tecniche')

	# e-commerce
	pubblicare_online = fields.Boolean(string="Pubblicare Prestashop")
	link_prestashop = fields.Char(string="Link Prestashop")
	#pubblicare_prestashop = fields.Boolean(string="Pubblicare on-line")

	pubblicare_amazon = fields.Boolean(string="Pubblicare Amazon")
	link_amazon = fields.Char(string="Link Amazon", size=200)

	pubblicare_ebay = fields.Boolean(string="Pubblicare eBay")
	link_ebay = fields.Char(string="Link eBay", size=200)

	pubblicare_wordpress = fields.Boolean(string="Pubblicare WordPress")
	link_wordpress = fields.Char(string="Link WordPress", size=200)

	funzioni = fields.Text('Elenco funzioni', help='Elencare le funzioni del prodotto nel formato "caratteristica=valore" (es: Dimensioni=15 pollici). Una caratteristica per ogni riga')
	descrizione_web = fields.Html('Descrizione web', size=200)

	default_code_padre = fields.Char(string="Rif. interno padre")
	descrizione_breve = fields.Html(string="Descrizione breve")
	descrizione_lunga = fields.Html(string="Descrizione lunga")

	disp_vendita_ecommerce = fields.Integer(string="Disp.vendita ecommerce")

