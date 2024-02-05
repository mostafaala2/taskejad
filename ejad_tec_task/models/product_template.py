from odoo import api,_, models,fields
from odoo.exceptions import ValidationError


class Product(models.Model):
    _inherit = "product.product"
    def send_notification(self,product_id):
        product = self.browse(product_id)
        #notfication to send to stock man

class ProductTemplate(models.Model):
    _inherit = "product.template"
    has_rop = fields.Boolean(string='Has ROP')
    rop_count = fields.Integer(string='ROP Count')

    def get_rop(self):
        pass
