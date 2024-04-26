from odoo import models, fields

class SchoolClass(models.Model):
    _name = 'eschool.class'
    _description = 'Class'

    name = fields.Char(string='Nom', required=True)
    prof_principal = fields.Text(string='Professeur Principal')
    student_ids = fields.One2many('eschool.student', 'class_id', string='Elèves')
    course_id = fields.Many2many('eschool.course', string='Cours')
   # teacher_id = fields.Many2one('school.teacher', string='Teacher')

