from datetime import datetime
from decimal import Decimal

import requests
from currencies.models import Currency, Rate
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    _url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    _fields = {
        'currency': 'Valute',
        'name': 'Name',
        'nominal': 'Nominal',
        'value': 'Value',
        'date': 'Date',
    }

    def handle(self, *args, **options):
        request = requests.get(self._url)
        if not request.status_code == requests.codes.ok:
            return 'Не удалось получить данные ЦБР.'
        rates_date = request.json()[self._fields['date']]
        for key, value in request.json()[self._fields['currency']].items():
            currency = Currency.objects.get_or_create(
                name=value[self._fields['name']],
                charcode=key,
            )
            Rate.objects.get_or_create(
                currency=currency[0],
                nominal=int(value[self._fields['nominal']]),
                value=Decimal(value[self._fields['value']]),
                date=datetime.fromisoformat(rates_date).date(),
            )
