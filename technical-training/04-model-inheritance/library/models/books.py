# -*- coding: utf-8 -*-
from odoo import models, fields

class Books(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title')
    __authors_ids = fields.Many2many('library.partner', string="Authors")
    edition_date =  fields.Date(string='Edition date',)
    isbn = fields.Char(string='ISBN')
    publisher_id = fields.Many2one('library.publisher', string='Publisher')

class BookCopy(models.Model):

    _name = 'library.book.copy'
    _inherits = {'library.book':'book_id'}
    copy_name = fields.Char('Book Copy Name',default=lambda r:r.env['ir.sequence'].next_by_code('BOOKCPY'))
    book_id = fields.Many2one('library.book',string='Original Book')
    rental_ids = fields.One2many('library.rental', 'book_id', string='Rentals')
