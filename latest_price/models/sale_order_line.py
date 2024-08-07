from odoo import fields, models, api


class sale_order_line(models.Model):

    _inherit = 'sale.order.line'

    latest_price = fields.Float(string='Latest Sale Price', compute="_compute_latest", store=True)



    def _get_latest_price(self, partner_id, product_id):
        records = self.search([
            ('product_id', '=', product_id.id),
            ('order_id.partner_id', '=', partner_id.id),
            ('order_id.state', 'in', ['sale', 'done'])
        ], order='create_date desc', limit=1)

        if records:
            return records.price_unit
        else:
            return 0

    @api.depends('product_template_id', 'order_id.partner_id')
    def _compute_latest(self):
        for record in self:
            if record.order_id.partner_id and record.product_id:
                record.latest_price = self._get_latest_price(record.order_id.partner_id, record.product_id)
            else:
                record.latest_price = 0