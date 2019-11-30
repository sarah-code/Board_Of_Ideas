 -*- coding: utf-8 -*-

from odoo import models, fields, api

class board_of_ideas(models.Model):
    _name = 'board_of_ideas.board_of_ideas'

    date = fields.Date(string="Date")
    idea = fields.Text(string="Idea/Area of Improvement")
    dep = fields.Text(string="department")
    login = fields.Many2one(string="Login", comodel_name="res.partner")
    resp = fields.Text(string="Response")
    owner = fields.Many2one(string="Owner", comodel_name="res.partner")
    resp_date = fields.Date(string="Response date")
    state = fields.Selection(string="Status", selection="[('draft','Draft'),('proposed','Proposed'),('onit','Working on'),('implemented','Implemented'),('rejected','Rejected')],"
    description = fields.Text()
