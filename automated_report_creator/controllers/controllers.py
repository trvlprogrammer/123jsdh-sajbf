# -*- coding: utf-8 -*-
from odoo import http

# class Skp/automatedReportCreator(http.Controller):
#     @http.route('/skp/automated_report_creator/skp/automated_report_creator/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/skp/automated_report_creator/skp/automated_report_creator/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('skp/automated_report_creator.listing', {
#             'root': '/skp/automated_report_creator/skp/automated_report_creator',
#             'objects': http.request.env['skp/automated_report_creator.skp/automated_report_creator'].search([]),
#         })

#     @http.route('/skp/automated_report_creator/skp/automated_report_creator/objects/<model("skp/automated_report_creator.skp/automated_report_creator"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('skp/automated_report_creator.object', {
#             'object': obj
#         })