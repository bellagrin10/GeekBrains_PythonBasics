from datetime import date
from decimal import Decimal

from task_4_3 import DICTIONARY_OF_EXCHANGE_RATES, DATE_OF_EXCHANGE_RATE


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
