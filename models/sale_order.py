from odoo import api, fields, models, _


class sale_order_template(models.Model):
    _inherit = "sale.order"

    testo_sconto_detrazione = fields.Html('Testo sconto detrazione')
    
    def send_email_by_tag(self, record, env, email_from):

        # Se il cliente ha un indirizzo di mail specificato
        if record['partner_id']['email'] and record['partner_id']['email'] != '':

            # Cerco i tag dell'ordine
            for tag in record['tag_ids']:
                tagName = tag['name'].upper()

                # Se esiste il tag Spedito
                if tagName != 'GLS' and tagName != 'PLX': continue

                # Cerco il numero del tracking
                trackNumber = ''
                trackNumberLink = ''

                pickings = env['stock.picking'].sudo().search([('sale_id', '=', record['id'])])
                for picking in pickings:
                    if 'codice_tracking_spedizione' in picking and picking['codice_tracking_spedizione']:
                        trackNumber = picking['codice_tracking_spedizione']

                if (trackNumber != '' and tagName == 'GLS'):
                    # GLS ha il link per il tracking
                    trackNumberLink = '<a href="https://www.gls-italy.com/?option=com_gls&view=track_e_trace&mode=search' \
                                      '&numero_spedizione=%s&tipo_codice=nazionale">Clicca qui per seguire la spedizione</a><br>' % (trackNumber)


                # Creo il body della mail (specificando il numero del tracking se è previsto nelle spedizioni)
                body = 'Salve, %s <br>' \
                       '<br>Le comunico che il suo ordine %s è stato evaso, <br>' \
                       'La spedizione avviene tramite corriere: %s <br>' \
                       '%s' \
                       '<br>Il codice di tracciabilità è %s<br>' \
                       '<br>Per qualsiasi problema legato alla spedizione potrà contattare un nostro operatore che tempestivamente provvederà alla risoluzione del problema. <br>' \
                       ' - Le nostre spedizioni sono tutte assicurate per garantire ai nostri clienti maggiore tranquillità nel caso di smarrimento o danneggiamento del collo, quindi apponete sempre la firma con “riserva specifica” al momento della consegna, questo consentirà una maggiore tutela anche dopo l’apertura del pacco. <br>' \
                       ' - Per riserva specifica si intende che bisogna controllare il pacco davanti al corriere, senza aprirlo, e qualora ci fosse una minima rottura scrivere nella riserva la specifica dell’anomalia riscontrata. <br>' \
                       '<br>Le contestazioni devono avvenire entro e non oltre 6gg calendariali dalla consegna della merce, inviando una mail a sinistri@gm-termoidraulica.it, con i seguenti dati: <br>' \
                       ' - Codice di spedizione del corriere <br>' \
                       ' - Nome e Cognome <br>' \
                       ' - Numero ordine per ordini <br>' \
                       ' - Dichiarazione dettagliata dell\'anomalia riscontrata e foto in allegato <br>' \
                       'Tutti i problemi che potrebbero insorgere sono risolvibili contattando i seguenti numeri <br>' \
                       'Phone: 0984524856 o inviando una mail a info@gm-termoidraulica.it <br>' \
                       ' <br>Distinti saluti <br>' \
                       'GM-Termoidraulica <br>' % (record['partner_id']['name'], record['display_name'], tagName, trackNumberLink, trackNumber)

                # Invio la mail
                mail_values = {
                    'subject': 'Ordine %s spedito' % record['display_name'],
                    'body_html': body,
                    'email_to': record['partner_id']['email'],
                    'email_from': email_from,
                }
                create_and_send_email = env['mail.mail'].create(mail_values).send()

                # Registro la mail inviata nelle note dell'ordine
                record.message_post(body=body)

                # Rimuovo il tag "In spedizione"
                record['tag_ids'] = [(3, int(tag['id']))]

                # Aggiungo il tag Spedito
                crmTagEnv = env["crm.tag"]
                tagSpeditoName = 'Spedito %s' % (tagName)
                tagSpedito = crmTagEnv.sudo().search([('name', '=', tagSpeditoName)], limit=1)
                if tagSpedito and len(tagSpedito) == 1:
                    record['tag_ids'] = [(4, int(tagSpedito[0]['id']))]
                break

    @api.onchange('sale_order_template_id')
    def onchange_testo_sconto(self):
        if self.sale_order_template_id:
            new_testo = ""
            if self.sale_order_template_id.testo_sconto_detrazione:
                new_testo = self.sale_order_template_id.testo_sconto_detrazione
            return self.update({'testo_sconto_detrazione':new_testo})


class report_sale_order(models.AbstractModel):
    _name = 'report.sale.report_saleorder'
    _description = 'Stampa report sale-order'

    def _get_report_values(self, docids, data=None):
        """Aggiunge l'etichetta 'Stampato' all'ordine"""

        docs = self.env['sale.order'].browse(docids)
        if not 'force_email' in self._context:
            for doc in docs:
                tag = self.env['crm.tag'].search([('name', '=', 'Stampato')], limit=1)
                if not tag:
                    tag = tag.create({'name': 'Stampato'})
                if tag.id not in doc.tag_ids.ids:
                    doc.tag_ids = [(4, tag.id)]
        return {
            'doc_ids': docs.ids,
            'doc_model': 'sale.order',
            'docs': docs
        }

