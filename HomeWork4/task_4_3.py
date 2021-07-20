import requests
from bs4 import BeautifulSoup
from decimal import Decimal
from datetime import date


def currency_rates(currency_code):
    """
    The function takes a currency code (for example, USD, EUR, GBP, ...)
    as an argument and returns:
    - the rate of this currency in relation to the ruble;
    - the date of exchange rate.
    :param currency_code: str - currency code
    :return: tuple(Decimal, date)
    - using Decimal so that the result is saved exactly;
      (if using float - the result will be the nearest binary floating point number);
    - the date must be in the form of a date object.
    """
    currency_code = currency_code.upper()
    currency_against_the_ruble = DICTIONARY_OF_EXCHANGE_RATES.get(currency_code)
    if currency_against_the_ruble:
        day, month, year = map(int, DATE_OF_EXCHANGE_RATE.split('.'))
        date_ = date(day=day, month=month, year=year)
        return Decimal(currency_against_the_ruble.replace(',', '.')), date_


def print_info(info):
    if info:
        print(*info)
    else:
        print(info)


response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

# print(response.status_code)

response.headers.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

# Extraction of all currency information.
currencies = soup.findAll('valute')

# Creating a dictionary of currencies in the format "currency code": "value".
DICTIONARY_OF_EXCHANGE_RATES = {currency.find('charcode').text: currency.find('value').text
                                for currency in currencies}

# Extraction the date that is passed in the server response.
DATE_OF_EXCHANGE_RATE = soup.find('valcurs').attrs['date']

if __name__ == '__main__':
    dollar_to_ruble_exchange_rate = currency_rates('USD')
    print_info(dollar_to_ruble_exchange_rate)

    euro_to_ruble_exchange_rate = currency_rates('EUR')
    print_info(euro_to_ruble_exchange_rate)

    print_info(currency_rates('eur'))
    print_info(currency_rates('xxx'))
