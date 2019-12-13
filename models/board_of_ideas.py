from odoo import models, fields, api, _
from datetime import datetime

class board_of_ideas(models.Model):
    _name = 'board.of.ideas'

    title = fields.Text(string="Title", readonly=1, default=lambda self: _('New'))

    date = fields.Date(string="Date", default=datetime.today())
    idea = fields.Text(string="Idea/Area of Improvement")
    dep = fields.Text(string="department")
    login = fields.Many2one(string="Login", comodel_name="res.partner", default=lambda self: self.env.user.id)

    owner = fields.Many2one(string="Owner", comodel_name="res.partner")
    resp_date = fields.Date(string="Response date")
    resp = fields.Text(string="Response")
    state = fields.Selection(string="Status", selection=[('draft','Draft'),('proposed','Proposed'),('onit','Working on'),('implemented','Implemented'),('rejected','Rejected')], default="draft")
    int_notes = fields.Html(string="Internal Notes")

    def name_get(self):
        data = []
        for rec in self:
            title = "ISSUE-%s" % (rec.id)
            data.append((rec.id, title))
        return data
    




