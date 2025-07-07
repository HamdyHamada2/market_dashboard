{
    'name': 'TradingView Clone',
    'version': '1.0',
    'summary': 'Real-time Market Intelligence Platform',
    'description': """
        Comprehensive TradingView-like platform with real-time market data,
        charts, news, events, and watchlists integrated with Odoo 18.
    """,
    'author': 'Hamdy Hamada',
    'category': 'Finance',
    'depends': [
        'base',
        'web',
        'website',
        'auth_signup',
        'website_forum'
    ],
    'data': [
        # ملفات الأمان أولاً
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        
        # البيانات الثابتة
        'data/cron_jobs.xml',
        
        # ملفات العروض
        'views/symbol_views.xml',
        'views/ohlc_views.xml',
        'views/technical_views.xml',
        'views/news_views.xml',
        'views/event_views.xml',
        'views/watchlist_views.xml',
        'views/templates.xml',
            
    ],
    'qweb': [
        'static/src/xml/charting_template.xml',
        'static/src/xml/symbol_detail_template.xml',
        'static/src/xml/market_explorer_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'tradingview_clone/static/src/js/charting.js',
            'tradingview_clone/static/src/scss/style.scss',
        ],
    },
    'installable': True,  # تأكد من وجود هذا الحقل
    'application': True,
    'license': 'LGPL-3',
    'auto_install': False,
}