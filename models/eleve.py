# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _



class eleve(models.Model):
    _name = "eleve"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    matricule = fields.Integer(string="Matricule")
    name = fields.Char(string="Nom et Prènom")
    sexe = fields.Selection([('garçon','Garçon'),('fille','Fille')],string="Sexe")
    date_naissance = fields.Date(string="Date de naissance")
    Adresse = fields.Char(string="Adresse")
    telephone = fields.Integer(String="Téléphone",size="8")


