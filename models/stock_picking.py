# -*- coding: utf-8 -*-

from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    @api.model
    def create(self, vals):
        # If we confirm a Purchase Order, the stock move will be created with the Order Date
        # Change the stock move date to use the Purchase Order Line scheduled date instead so we get accurate results from the forecast
        if ('state' not in vals or vals['state'] != 'done') and 'date_expected' in vals:
            vals['date'] = vals['date_expected']

        return super(StockMove, self).create(vals)

    @api.multi
    def write(self, vals):
        # Update PO scheduled date will update date_expected by default, update date as well
        if ('state' not in vals or vals['state'] != 'done') and 'date_expected' in vals:
            vals['date'] = vals['date_expected']

        return super(StockMove, self).write(vals)
