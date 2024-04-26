from odoo import models, fields

class Teacher(models.Model):
    _name = 'eschool.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Nom', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Genre', default='male')
    birthdate = fields.Date(string='Date de Naissance')
    address = fields.Text(string='Addresse')
    phone = fields.Char(string='Telephone')
    email = fields.Char(string='Email')
    course_id = fields.Many2many('eschool.course', string='Cours')
    #class_ids = fields.Many2many('school.class', string='Classes Taught')
