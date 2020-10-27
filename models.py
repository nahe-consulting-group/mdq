from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def update_mdq(self):
        products = self.env['product.product'].search([('name','=','ADAPTADOR BLUETOOTH 4.0 USB - OEM TP-7183')])
        #products = self.env['product.product'].search([('currency_id','=',1)])
        for product in products:
            product.list_price = product.list_price / 90
            product.force_currency_id = 3
