from odoo import models, fields

class product_product(models.Model):
    _inherit = 'product.product'
    last_purchase_price = fields.Float(string="Last purchase price", default=0)