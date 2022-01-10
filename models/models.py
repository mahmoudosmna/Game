# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WindowsGame(models.Model):
    _name = 'game.game'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    # Field Definition

    name = fields.Char(string="Name", required=True)
    win_loss = fields.Selection(string="Wines/Losses", selection=[
        ('win', 'Wines'), ('loss', 'Losses'), ], required=False)
    duration = fields.Float(string="Duration", required=True)
    number_of_game = fields.Integer(string="Number Of Game", required=True, )
