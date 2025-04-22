from odoo import models, api, fields, _
from odoo.exceptions import UserError

class Promotion(models.Model):
    _name = 'retail.promotion'
    _rec_name = "name"
    _description = 'Retail Promotion'

    name = fields.Char(string='Nombre', required=True)
    is_active = fields.Boolean(string='Activo', default=True)
    discount = fields.Float(string='Descuento (%)', required=True)
    start_date = fields.Date(string='Inicio', required=True)
    end_date = fields.Date(string='Fin', required=True)
    product_ids = fields.Many2many('product.product', string='Productos')