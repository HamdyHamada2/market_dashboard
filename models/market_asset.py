from odoo import models, fields

class MarketAsset(models.Model):
    _name = 'market.asset'
    _description = 'Market Asset'

    name = fields.Char(required=True)
    symbol = fields.Char(required=True)
    asset_type = fields.Selection([
        ('stock', 'Stock'),
        ('crypto', 'Cryptocurrency'),
        ('forex', 'Forex'),
    ], string="Asset Type", required=True)
    current_price = fields.Float(string="Current Price", digits=(16, 6))
