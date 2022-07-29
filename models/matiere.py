# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _



class matiere(models.Model):
    _name = "matiere"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Nom du matière")
    type = fields.Selection([("Théorique","Théorique"),("Pratique","Pratique")],string="Type")
    Coff = fields.Float(string="Coefficient")
    nombre_heures = fields.Float(string="Nombre des heures par semaine")