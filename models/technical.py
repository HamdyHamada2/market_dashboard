from odoo import models, fields

class TradingViewTechnicalIndicator(models.Model):
    _name = 'tradingview.technical'
    _description = 'Technical Indicators'

    symbol_id = fields.Many2one('tradingview.symbol', string='Symbol', required=True)
    indicator_name = fields.Char(string='Indicator Name', required=True)
    value = fields.Float(string='Value')
    signal = fields.Selection([
        ('buy', 'Buy'),
        ('sell', 'Sell'),
        ('neutral', 'Neutral'),
    ], string='Signal', default='neutral')
    timestamp = fields.Datetime(string='Timestamp', required=True)
