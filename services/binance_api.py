import requests

class BinanceAPIService:
    BASE_URL = "https://api.binance.com/api/v3/ticker/price"

    @staticmethod
    def get_price(symbol):
        # Binance يستخدم رموز زي BTCUSDT وليس BTCUSD
        binance_symbol = symbol.upper().replace('USD', 'USDT')
        response = requests.get(BinanceAPIService.BASE_URL, params={'symbol': binance_symbol})
        if response.status_code == 200:
            data = response.json()
            return float(data['price'])
        else:
            return None
