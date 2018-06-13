# -*- coding: utf-8 -*-

from odoo import models, fields, api


    
class Student(models.Model):
    _name = 'student_i_s.student'
    name = fields.Char()
    fname = fields.Char()
    age = fields.Integer()
    address = fields.Char()