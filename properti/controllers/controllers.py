# -*- coding: utf-8 -*-
# from odoo import http


# class Properti(http.Controller):
#     @http.route('/properti/properti', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/properti/properti/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('properti.listing', {
#             'root': '/properti/properti',
#             'objects': http.request.env['properti.properti'].search([]),
#         })

#     @http.route('/properti/properti/objects/<model("properti.properti"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('properti.object', {
#             'object': obj
#         })
