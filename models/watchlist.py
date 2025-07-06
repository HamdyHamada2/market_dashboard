from odoo import models, fields

class TradingViewWatchlist(models.Model):
    _name = 'tradingview.watchlist'
    _description = 'User Watchlist'

    name = fields.Char(string='Watchlist Name', required=True)
    user_id = fields.Many2one('res.users', string='User')
    symbol_ids = fields.Many2many('tradingview.symbol', string='Tracked Symbols')
