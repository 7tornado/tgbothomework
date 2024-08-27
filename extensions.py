#все классы исключений

import requests
import json

class APIException(Exception):
    """Класс для обработки исключений при работе с API"""
    pass

class Converter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        # Словарь для хранения допустимых валют
        keys = {
            'евро': 'EUR',
            'доллар': 'USD',
            'рубль': 'RUB',
        }

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {quote}.')

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}.')

        # Запрос к API для получения курса валют
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[base_ticker]

        return total_base * amount
