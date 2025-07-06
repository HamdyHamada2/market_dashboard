from odoo import models, fields

class TradingViewEvent(models.Model):
    _name = 'tradingview.event'
    _description = 'Market Events'

    name = fields.Char(string='Event Name', required=True)
    description = fields.Text(string='Description')
    date = fields.Datetime(string='Event Date')
    country = fields.Char(string='Country')
    symbol_id = fields.Many2one('tradingview.symbol', string='Related Symbol')
