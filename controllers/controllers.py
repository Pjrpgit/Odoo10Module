# -*- coding: utf-8 -*-
from odoo import http

# class FctBarajas(http.Controller):
#     @http.route('/fct_barajas/fct_barajas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fct_barajas/fct_barajas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fct_barajas.listing', {
#             'root': '/fct_barajas/fct_barajas',
#             'objects': http.request.env['fct_barajas.fct_barajas'].search([]),
#         })

#     @http.route('/fct_barajas/fct_barajas/objects/<model("fct_barajas.fct_barajas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fct_barajas.object', {
#             'object': obj
#         })