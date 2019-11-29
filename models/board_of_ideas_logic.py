 -*- coding: utf-8 -*-

from odoo import models, fields, api

class board_of_ideas(models.Model):
    _name = 'board_of_ideas.board_of_ideas'

    date = fields.Date(string="Date")
    idea = fields.Text(string="Idea/Area of Improvement")
    dep = fields.Text(string="department")
    login = fields.Many2one(string="Login", comodel_name="res.partner")
    acts = fields.Text(string="Definition of actions")
    owner = fields.Many2one(string="Owner")
    state = fields.Selection(
    description = fields.Text()
