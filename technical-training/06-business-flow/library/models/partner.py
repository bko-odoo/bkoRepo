# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Partner(models.Model):
    _inherit = 'res.partner'

    author =  fields.Boolean('is an Author', default=False)
    publisher =  fields.Boolean('is a Publisher', default=False)
    rental_ids = fields.One2many(
        'library.rental',
        'customer_id',
        string='Rentals')
    book_ids = fields.Many2many(
        comodel_name="product.product",
        string="Books",
        domain=[('book','=',True), ],
    )
    nationality_id = fields.Many2one(
        'res.country',
        'Nationality',
    )
    to_pay = fields.Float('To Pay', compute = '_total_price')
    birthdate =  fields.Date('Birthdate',)
    @api.depends
    def _total_price(self):
        for p in self:
            total = 0
            for cost in p.rental_ids:
                total = total+cost.rental_cost
            self.to_pay = total

