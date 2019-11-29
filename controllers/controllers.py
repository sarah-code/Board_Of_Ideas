# -*- coding: utf-8 -*-
from odoo import http

# class BoardOfIdeas(http.Controller):
#     @http.route('/board_of_ideas/board_of_ideas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/board_of_ideas/board_of_ideas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('board_of_ideas.listing', {
#             'root': '/board_of_ideas/board_of_ideas',
#             'objects': http.request.env['board_of_ideas.board_of_ideas'].search([]),
#         })

#     @http.route('/board_of_ideas/board_of_ideas/objects/<model("board_of_ideas.board_of_ideas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('board_of_ideas.object', {
#             'object': obj
#         })