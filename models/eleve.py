from odoo import models, fields

class Student(models.Model):
    _name = 'eschool.student'
    _description = 'Student'

    name = fields.Char(string='Nom', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Genre', default='male')
    birthdate = fields.Date(string='Date de naissance')
    address = fields.Text(string='Addresse')
    phone = fields.Char(string='Telephone')
    email = fields.Char(string='Email')
    class_id = fields.Many2one('eschool.class', string='Classe')


"""class SchoolClass(models.Model):
    _name = 'eschool.class'
    _description = 'Class'

    name = fields.Char(string='Name', required=True)
    #teacher_id = fields.Many2one('school.teacher', string='Teacher')
    student_ids = fields.One2many('eschool.student', 'class_id', string='Students')
"""