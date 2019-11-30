

from odoo import models, fields, api

class board_of_ideas(models.Model):
    _name = 'board.of.ideas'

    date = fields.Date(string="Date")
    idea = fields.Text(string="Idea/Area of Improvement")
    dep = fields.Text(string="department")
    login = fields.Many2one(string="Login", comodel_name="res.partner")

    owner = fields.Many2one(string="Owner", comodel_name="res.partner")
    resp_date = fields.Date(string="Response date")
    resp = fields.Text(string="Response")
    state = fields.Selection(string="Status", selection=[('draft','Draft'),('proposed','Proposed'),('onit','Working on'),('implemented','Implemented'),('rejected','Rejected')], default="draft")
    int_notes = fields.Html(string="Internal Notes")

