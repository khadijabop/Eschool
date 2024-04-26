from odoo import models, fields

class Course(models.Model):
    _name = 'eschool.course'
    _description = 'Course'

    name = fields.Char(string='Nom', required=True)
    description = fields.Text(string='Description')
    teacher_id = fields.Many2many('eschool.teacher', string='Teacher')
    class_id = fields.Many2many('eschool.class', string='Classe')
    #class_id = fields.Many2one('school.class', string='Class')
