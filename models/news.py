from odoo import models, fields

class TradingViewNews(models.Model):
    _name = 'tradingview.news'
    _description = 'Market News'

    title = fields.Char(string='Title', required=True)
    content = fields.Text(string='Content')
    published_date = fields.Datetime(string='Published Date')
    source = fields.Char(string='Source')
    symbol_id = fields.Many2one('tradingview.symbol', string='Related Symbol')
