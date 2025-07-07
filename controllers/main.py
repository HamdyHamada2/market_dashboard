from odoo import http
from odoo.http import request
from datetime import datetime, timedelta
import json

class TradingViewController(http.Controller):
    
    @http.route('/market', type='http', auth="public", website=True)
    def market_explorer(self, **kwargs):
        symbols = request.env['tradingview.symbol'].sudo().search([
            ('active', '=', True)
        ])
        return request.render('tradingview_clone.market_explorer', {
            'symbols': symbols
        })

    @http.route('/market/<string:symbol_slug>', type='http', auth="public", website=True)
    def symbol_detail(self, symbol_slug, **kwargs):
        symbol = request.env['tradingview.symbol'].sudo().search([
            ('slug', '=', symbol_slug),
            ('active', '=', True)
        ], limit=1)

        if not symbol:
            return request.not_found()

        date_from = datetime.now() - timedelta(days=7)
        ohlc_data = request.env['tradingview.ohlc'].sudo().search([
            ('symbol_id', '=', symbol.id),
            ('timestamp', '>=', date_from.strftime('%Y-%m-%d')),
            ('interval', '=', '1d')
        ], order='timestamp asc')

        return request.render('tradingview_clone.symbol_detail', {
            'symbol': symbol,
            'ohlc_data': ohlc_data
        })

    @http.route('/market/<slug:symbol>', type='http', auth='public', website=True)
    def symbol_detail(self, symbol, **kwargs):
        symbol_obj = request.env['market.symbol'].sudo().search([('slug', '=', symbol)], limit=1)
        ohlc = request.env['market.ohlc'].sudo().search([('symbol_id', '=', symbol_obj.id)], order="timestamp asc")

        ohlc_data = [{
            'time': int(o.timestamp.timestamp()),
            'open': o.open,
            'high': o.high,
            'low': o.low,
            'close': o.close,
        } for o in ohlc]

        return request.render('tradingview_clone.symbol_detail', {
            'symbol': symbol_obj,
            'ohlc_data_json': json.dumps(ohlc_data),
        })