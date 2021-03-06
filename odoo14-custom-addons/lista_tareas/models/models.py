# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class lista_tareas(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
    avatar = fields.Image('Imagen tarea', max_width = 50, max_heigth = 50)
    tarea = fields.Char()
    fecha = fields.Date()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_pc", store=True)
    realizada = fields.Boolean()
    campo_prueba = fields.Text()
    descripcion = fields.Text()
    #Este computo depende de la variable prioridad
    @api.depends('prioridad')
    #Funcion para calcular el valor de urgente
    def _value_pc(self):
        #Para cada registro
        for record in self:
            #Si la prioridad es mayor que 8, se considera urgente, en otro caso no lo es
            if record.prioridad>8:
                record.urgente = True
            else:
                record.urgente = False
