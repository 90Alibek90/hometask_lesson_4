import requests
from decimal import *
from datetime import *
def currency_rate(val):
    val = val.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if val not in response:
        return None


    rub = response[response.find('<Value>', response.find(val)) + 7:response.find('</Value>', response.find(val))]
    day_raw = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, day_raw)
    return f"Курс {val}, на {datetime(day=day, month=month, year=year)} является {Decimal(rub.replace(',', '.'))}"

# print(currency_rate('USD'))
