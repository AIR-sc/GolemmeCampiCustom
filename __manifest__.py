# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': "Golemme custom fields",
    'version': "1.0.0.0",
    'author': "AIR-sc",
    'summary': 'Consente di specificare alcuni campi custom nell''elenco dei proditti',
    'description' : 'Consente di specificare alcuni campi custom come marca,tecnologia, btu, modello, etc... nei prodotti',
    'license':'OPL-1',
    'category': "Extra Tools",
    'data':[
             'views/product_form_custom_fields.xml',
             'views/menu.xml',
             'data/golemme.classe.csv',
             'data/golemme.marca.csv',
             'data/golemme.tecnologia.csv',
             'data/golemme.telecomando.csv',
             'data/golemme.tipologia_installazione.csv',
             'data/golemme.tipologia.csv',
             'data/golemme.unita.csv',
             'security/ir.model.access.csv',
             ],
    'website': 'https://www.air-srl.com',
    'depends': ['stock'],
    'installable': True,
    'auto_install': False,
	"images":['static/description/golemmeLogo.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
