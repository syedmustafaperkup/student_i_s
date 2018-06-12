# -*- coding: utf-8 -*-
from odoo import http

# class StudentIS(http.Controller):
#     @http.route('/student_i_s/student_i_s/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/student_i_s/student_i_s/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('student_i_s.listing', {
#             'root': '/student_i_s/student_i_s',
#             'objects': http.request.env['student_i_s.student_i_s'].search([]),
#         })

#     @http.route('/student_i_s/student_i_s/objects/<model("student_i_s.student_i_s"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student_i_s.object', {
#             'object': obj
#         })