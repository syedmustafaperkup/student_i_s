# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class student_i_s(models.Model):
#     _name = 'student_i_s.student_i_s'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class Teacher(models.Model):
    _name = 'student_i_s.teacher'
    name = fields.Char()
    qualification = fields.Char()
    specialty = fields.Char()

class Student(models.Model):
    _name = 'student_i_s.student'
    name = fields.Char()
    fname = fields.Char()
    age = fields.Integer()
    address = fields.Char()

class Course(models.Model):
    _name = 'student_i_s.course'
    name = fields.Char()
    specialty_id = fields.Many2one('student_i_s.teacher', ondelete='cascade',string="Teacher",required=True)

class Assign(models.Model):
    _name = 'student_i_s.assign'
    name= fields.Char()
    course_id = fields.Many2one('student_i_s.course',
        ondelete='cascade', string="Course Name", required=True)
    student_id = fields.Many2one('student_i_s.student',
        ondelete='cascade', string="Student", required=True)