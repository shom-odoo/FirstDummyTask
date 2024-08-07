from odoo import models, fields


class purchase_order(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        for record in self:
            for order in record.order_line:
                order.product_id.last_purchase_price = order.price_unit

        return super().button_confirm()
