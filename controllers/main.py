from odoo import http
from odoo.http import request
from datetime import datetime, timedelta

class TradingViewController(http.Controller):
    
    @http.route('/market', type='http', auth="public", website=True)
    def market_explorer(self, **kwargs):
        symbols = request.env['tradingview.symbol'].sudo().search([('active', '=', True)])
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
        
        # جلب بيانات السعر (OHLC) للأيام السبعة الماضية
        date_from = datetime.now() - timedelta(days=7)
        ohlc_data = request.env['tradingview.ohlc'].sudo().search([
            ('symbol_id', '=', symbol.id),
            ('timestamp', '>=', date_from.strftime('%Y-%m-%d')),
            ('interval', '=', '1d')  # بيانات يومية
        ], order='timestamp asc')
            
        return request.render('tradingview_clone.symbol_detail', {
            'symbol': symbol,
            'ohlc_data': ohlc_data
        })