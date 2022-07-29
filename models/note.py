# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _



class professeur(models.Model):
    _name = "professeur"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    moyenne = fields.Float(string="Moyenne Générale")
    #appreciation= fields.
    rang = fields.Integer(String="Rang")
