from odoo import api, fields, models, _


class sale_order_template(models.Model):
    _inherit = "sale.order"

    testo_sconto_detrazione = fields.Html('Testo sconto detrazione')

    def send_email_by_tag(self, record, env, email_from):
        # Se il cliente ha un indirizzo di mail specificato
        if record['partner_id']['email'] and record['partner_id']['email'] != '':

            # Cerco i tag del cliente
            for tag in record['tag_ids']:
                # Se esiste il tag Spedito
                if tag['name'].lower() != 'spedito': continue

                # Cerco il numero del tracking
                trackNumber = ''
                pickings = env['stock.picking'].sudo().search([('sale_id', '=', record['id'])])

                for picking in pickings:
                    if 'codice_tracking_spedizione' in picking and picking['codice_tracking_spedizione']:
                        trackNumber += "<b>%s</b> " % picking['codice_tracking_spedizione']

                # Creo il body della mail (specificando il numero del tracking se è previsto nelle spedizioni)
                body = ''
                if trackNumber and trackNumber != '':
                    body = 'Ciao %s, <br>il tuo ordine <b>%s</b> è stato spedito, questo è il numero del tracking della spedizione: %s<br>Distinti saluti <br><br>AIR Servizio invio' % (
                    record['partner_id']['name'], record['display_name'], trackNumber)
                else:
                    body = 'Ciao %s, <br>il tuo ordine <b>%s</b> è stato spedito.<br>Distinti saluti <br><br>AIR Servizio invio' % (
                    record['partner_id']['name'], record['display_name'], trackNumber)

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

                break