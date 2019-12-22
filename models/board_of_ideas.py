from odoo import models, fields, api, _
from datetime import datetime

class board_of_ideas(models.Model):
    _name = 'board.of.ideas'
    _inherit = ['mail.thread','mail.activity.mixin']

    title = fields.Text(string="Title", store ="True", required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))

    sev = fields.Selection(string="Severnity", selection=[('0','O'),('1','!'),('2','!!'),('3','!!!'),('4','!!!!')], default="0", help='How to rate severnity?\n o means no immediate attention needed.\n ! means attention needed in a year.\n !! means attention needed in 6 months.\n !!! means attention needed in 3 months. \n !!!! means attention highly need in under 3 months.')
    date = fields.Date(string="Date", default=datetime.today())
    idea = fields.Text(string="Idea/Area of Improvement")
    dep = fields.Text(string="Department")
    login = fields.Many2one(string="Login", comodel_name="res.users", store="True", default=lambda self: self.env.user.id)

    owners = fields.Many2many(string="Owner(s)", comodel_name="res.users")
    resp_date = fields.Date(string="Response date")
    resp = fields.Text(string="Response")
    state = fields.Selection(string="Status", selection=[('draft','Draft'),('proposed','Proposed'),('onit','Working on'),('implemented','Implemented'),('rejected','Rejected')], default="draft")
    int_notes = fields.Html(string="Internal Notes")
    desc = fields.Html(string="Detailed description")

    @api.onchange('sev')
    def severnity_warning(self):
        for rec in self:
            if int(rec.sev) >= 3:
                return {
                   'warning': {
                        'title': _('Severnity level warning'),
                        'message': _('You are about to log an issue with severnity "'+ dict(self._fields['sev'].selection).get(self.sev) +' - ' + self.sev + '".\n Please be rethink how severe the issue really is or talk to you manager.')
                   }
                }

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
            vals['state'] = 'proposed'
        res = super().create(vals)
        return res

    def onit_progressbar(self):
        for rec in self:
            rec.write({
                'state': 'onit'
                })

    def implement_progressbar(self):
        for rec in self:
            rec.write({
                'state': 'implemented'
                })

    def reject_progressbar(self):
        for rec in self:
            rec.write({
                'state': 'rejected'
                })