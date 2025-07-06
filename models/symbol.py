from odoo import models, fields, api

class TradingViewSymbol(models.Model):
    _name = 'tradingview.symbol'
    _description = 'Financial Symbol'
    _rec_name = 'symbol'

    name = fields.Char(string='Asset Name', required=True)
    symbol = fields.Char(string='Symbol', required=True)
    slug = fields.Char(string='Slug', compute='_compute_slug', store=True)
    exchange = fields.Char(string='Exchange')
    region = fields.Char(string='Region')
    currency = fields.Char(string='Currency')
    sector = fields.Char(string='Sector')
    industry = fields.Char(string='Industry')
    isin = fields.Char(string='ISIN')
    type = fields.Selection([
        ('stock', 'Stock'),
        ('crypto', 'Cryptocurrency'),
        ('forex', 'Forex'),
        ('commodity', 'Commodity'),
        ('index', 'Index')
    ], string='Asset Type', default='stock')
    active = fields.Boolean(string='Active', default=True)

    current_price = fields.Float(string='Current Price', compute='_compute_current_price', store=True)
    daily_change = fields.Float(string='Daily Change (%)', compute='_compute_daily_change', store=True)

    @api.depends('symbol')
    def _compute_slug(self):
        for record in self:
            record.slug = (record.symbol or '').lower().replace('/', '-')

    def _compute_current_price(self):
        # لاحقًا هنربطه ببيانات OHLC أو API خارجي
        for record in self:
            record.current_price = 0.0

    def _compute_daily_change(self):
        # لاحقًا هنربطه بالتحليل البياني
        for record in self:
            record.daily_change = 0.0
