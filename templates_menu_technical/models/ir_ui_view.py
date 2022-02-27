# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

class View(models.Model):

    _inherit = "ir.ui.view"

    report_id = fields.Many2one('ir.actions.report', string="Report", compute="_compute_report_id", store=False)

    def _compute_report_id(self):
        for view in self:
            view.report_id = False
            reports = self.env['ir.actions.report'].search([])
            for report in reports:
                if report.report_name.split('.')[1] == view.name:
                    view.report_id = report