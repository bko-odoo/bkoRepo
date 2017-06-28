# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'
    _order = "rental_date desc,return_date desc"

    customer_id = fields.Many2one(
        'res.partner',
        'Customer',
        domain=[('customer','=',True), ],
        required=True,
    )
    book_id = fields.Many2one(
        'product.product',
        'Book',
        domain=[('book','=',True)],
        required=True,
    )
    state = fields.Selection(
        [('borrowed', 'Borrowed'), ('returned', 'Returned'), ('lost', 'Lost')],
        string='State', default='borrowed', track_visibility='onchange', readonly=False)
    rental_cost = fields.Float('Price' , compute='_calculate_price')
    rental_date =  fields.Date(string='Rental date', required=True, default=lambda self: fields.Date.today())
    return_date =  fields.Date(string='Return date', required=True)

    @api.depends('state')
    def _calculate_price(self):
        for rental in self:
            if rental.rental_date and rental.return_date:
                start_date = fields.Date.from_string(rental.rental_date)
                end_date = fields.Date.from_string(rental.return_date)
                returned_real_date = fields.Date.from_string(fields.Date.today())
                if rental.state == 'returned':
                    if returned_real_date == end_date:
                        rental.rental_cost = 0.0
                    else:
                        rental.rental_cost = (end_date - returned_real_date)*rental.book_id.rental_price
                elif rental.state == 'lost':
                    rental.rental_cost = rental.book_id.cost
                else:
                    rental.rental_cost = 0.0
            else:
                rental.rental_cost = 0.0