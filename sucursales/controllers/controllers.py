# -*- coding: utf-8 -*-
# from odoo import http


# class Sucursales(http.Controller):
#     @http.route('/sucursales/sucursales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sucursales/sucursales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sucursales.listing', {
#             'root': '/sucursales/sucursales',
#             'objects': http.request.env['sucursales.sucursales'].search([]),
#         })

#     @http.route('/sucursales/sucursales/objects/<model("sucursales.sucursales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sucursales.object', {
#             'object': obj
#         })
