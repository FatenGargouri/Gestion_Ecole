# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _



class professeur(models.Model):
    _name = "professeur"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    matricule = fields.Integer(string="Matricule")
    name = fields.Char(string="Nom et Prènom")
    cin= fields.Integer(String="Numéro Cin")
    sexe = fields.Selection([('Homme','Homme'),('Femme','Femme')],string="Sexe")
    date_naissance = fields.Date(string="Date de naissance")
    Adresse = fields.Char(string="Adresse")
    telephone = fields.Integer(String="Téléphone",size="8")
    email = fields.Char(string="E-mail")

