from odoo import fields, api, models, _ 
from odoo.exceptions import ValidationError, UserError
class SaleOrderLinePromotion(models.Model):
	_inherit = 'sale.order.line'

	promotion_id = fields.Many2one('retail.promotion', string='Promocion')

	def _convert_to_tax_base_line_dict(self):
		""" Convert the current record to a dictionary in order to use the generic taxes computation method
		defined on account.tax.

		:return: A python dictionary.
		"""
		self.ensure_one()
		promotion = self.env['retail.promotion'].search([
			('product_ids', 'in', self.product_id.id),
			('start_date', '<=', fields.Date.today()),
			('end_date', '>=', fields.Date.today()),
			('is_active', '=', True),
		], limit=1)

		return self.env['account.tax']._convert_to_tax_base_line_dict(
			self,
			partner=self.order_id.partner_id,
			currency=self.order_id.currency_id,
			product=self.product_id,
			taxes=self.tax_id,
			price_unit=self.price_unit,
			quantity=self.product_uom_qty,
			discount=promotion.discount if promotion else self.discount,
			price_subtotal=self.price_subtotal,
		)