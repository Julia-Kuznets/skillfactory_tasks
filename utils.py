
import requests

import json

from config import keys, API_KEY

class ConvertionException(Exception):
    pass

class CurrencyConvertor:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{quote_ticker}/{base_ticker}/{amount}')
        total_base = json.loads(r.content)['conversion_rate']

        return total_base

