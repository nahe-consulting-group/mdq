from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def update_mdq(self):
        products = self.env['product.product'].search([('id','=',7945)])
        for product in products:
            product.list_price = product.list_price / 90
