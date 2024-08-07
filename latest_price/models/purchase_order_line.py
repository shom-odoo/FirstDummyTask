from odoo import models, fields


class purchase_order_line(models.Model):
    _inherit = 'purchase.order.line'

    latest_price = fields.Float(string='Last Price', readonly=True, related='product_id.last_purchase_price')
