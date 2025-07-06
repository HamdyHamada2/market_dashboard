from odoo import models, fields

class TradingViewOHLC(models.Model):
    _name = 'tradingview.ohlc'
    _description = 'OHLC Price Data'
    _order = 'timestamp desc'

    symbol_id = fields.Many2one('tradingview.symbol', string='Symbol', required=True, ondelete='cascade')
    timestamp = fields.Datetime(string='Timestamp', required=True)
    open = fields.Float(string='Open')
    high = fields.Float(string='High')
    low = fields.Float(string='Low')
    close = fields.Float(string='Close')
    volume = fields.Float(string='Volume')
    interval = fields.Selection([
        ('1m', '1 Minute'),
        ('5m', '5 Minutes'),
        ('15m', '15 Minutes'),
        ('1h', '1 Hour'),
        ('4h', '4 Hours'),
        ('1d', '1 Day'),
        ('1w', '1 Week'),
    ], string='Interval', default='1d')
