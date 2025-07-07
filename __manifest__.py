{
    'name': 'TradingView Clone',
    'version': '1.0',
    'summary': 'Real-time Market Intelligence Platform',
    'description': """
        TradingView Clone is a fully integrated, real-time market intelligence platform built on Odoo 18.0.
        It provides dynamic charting, technical indicators, financial news, economic events, and user watchlists.
        Ideal for financial analysts, investors, and enthusiasts seeking an all-in-one dashboard.
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
        'data/symbol_demo_data.xml',
        'views/market_asset_views.xml',
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
    #'auto_install': False,
}