from odoo import models, fields, api, _
from datetime import datetime

class board_of_ideas(models.Model):
    _name = 'board.of.ideas'
    _inherit = ['mail.thread','mail.activity.mixin']

    title = fields.Text(string="Title", store ="True", required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))

    date = fields.Date(string="Date", default=datetime.today())
    idea = fields.Text(string="Idea/Area of Improvement")
    dep = fields.Text(string="Department")
    login = fields.Many2one(string="Login", comodel_name="res.partner", store="True", default=lambda self: self.env.user.id)

    owners = fields.Many2many(string="Owner(s)", comodel_name="res.partner")
    resp_date = fields.Date(string="Response date")
    resp = fields.Text(string="Response")
    state = fields.Selection(string="Status", selection=[('draft','Draft'),('proposed','Proposed'),('onit','Working on'),('implemented','Implemented'),('rejected','Rejected')], default="draft")
    int_notes = fields.Html(string="Internal Notes")



    def name_get(self):
        data = []
        for rec in self:
            title = self.title
            data.append((rec.id, title))
        return data
    
    @api.model
    def create(self, vals):
        if vals.get('title', _('New')) == _('New'):
            vals['title'] = self.env['ir.sequence'].next_by_code('code')
        res = super().create(vals)
        return res




