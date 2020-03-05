# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class fct_barajas(models.Model):
#     _name = 'fct_barajas.fct_barajas'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class fct_barajas_alumno(models.Model):
    _name = 'fct_barajas.alumno'

    name = fields.Char(string="Nombre",requiered=True,help="Introduzca el nombre del alumno")
    apellido = fields.Char(string="Apellido",requiered=True,help="Introduzca el apellido del alumno")
    fecha_nacimiento = fields.Date(string="Fecha Nacimiento",requiered=True)
    curso = fields.Selection([('0','17/18'),('1','18/19'),('2','19/20'),('3','20/21')],default="0",string="Curso lectivo",help="Inotroduzca el curso")
    telefono = fields.Integer(string="Teléfono")
    ciclo = fields.Selection([('0','DAM'),('1','DAW'),('2','ASIR')],string="Ciclo formativo",default="0")
    periodo = fields.Selection([('0','MARZO'),('1','SEPTIEMBRE')],string="Periodo",requiered=True,default="0")
    nota_media = fields.Float(string="Nota media decimal")
    nota = fields.Char(string="Nota expediente",compute="_tranform", store=True)
    empresa = fields.Many2one("fct_barajas.empresa",string="Empresa",requiered=True)

    @api.depends('nota_media')
    def _tranform(self):
        if self.nota_media < 6 :
            self.nota = "Aprobado"
        elif self.nota_media < 7 :
            self.nota="Bien"
        elif self.nota_media < 8 :
            self.nota = "Notable"
        else :
            self.nota = "Sobresaliente"


class fct_barajas_empresa(models.Model):
    _name = 'fct_barajas.empresa'

    name = fields.Char(string="Nombre Empresa",requiered=True,help="Introduzca el nombre de la empresa")
    contacto = fields.Char(string="Persona de contacto",requiered=True,help="Introduzca el nombre de la persona de contacto")
    email = fields.Char(string="Email persona contacto",requiered=True,help="Introduzca el email de la persona de contacto")
    telefono = fields.Char(string="Teléfono empresa",requiered=True)
    direccion = fields.Text(string="Direccion de la empresa")
    alumnos = fields.One2many("fct_barajas.alumno","empresa",string="Alumnos")
