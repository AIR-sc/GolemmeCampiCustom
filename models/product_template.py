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
	colore  = fields.Many2one('golemme.colore', string="Colore")
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
	link_schede_tecniche = fields.Text('Link schede tecniche')

	pubblicare_online = fields.Boolean(string="Pubblicare on-line")

	funzioni = fields.Text('Elenco funzioni', help='Elencare le funzioni del prodotto nel formato "caratteristica=valore" (es: Dimensioni=15 pollici). Una caratteristica per ogni riga')
	descrizione_web = fields.Html('Descrizione web')