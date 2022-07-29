# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _



class classe(models.Model):
    _name = "classe"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Nom du classe")
    description = fields.Char(string="Description")
