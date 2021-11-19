import requests
from decimal import *
from datetime import *
# date_str = "2021-11-19"
# currency_date = DT.datetime.strptime(date_str, '%Y-%m-%d').date()

getcontext().prec = 4

def currency_rate(val):
    val = val.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if val not in response:
        return None

    # find_currency = response.find(val)
    # cut_1 = response[find_currency::]
    #
    # start = cut_1.find('<Value')
    # cut_2 = cut_1[start::]
    #
    # end = cut_1.find('</Value>')
    # cut_3 = cut_1[end::]
    #
    # cut_4 = cut_1[start:end]
    #
    # final_cut = cut_4[7::]
    #
    # # float_1 = float(final_cut.replace(',', '.').strip("'"))
    # decimal_1 = Decimal(final_cut.replace(',', '.'))
    # # return f'Курс {val} на {currency_date} является {float_1} руб'
    # return f'Курс {val} на {currency_date} является {decimal_1} руб'

# print(currency_rate('USD'))
# print(currency_rate('EUR'))
# print(currency_rate('KZT'))
# print(currency_rate(input('Введите название валюты: ')))

    rub = response[response.find('<Value>', response.find(val)) + 7:response.find('</Value>', response.find(val))]
    day_raw = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, day_raw)
    return f"Курс {val}, на {datetime(day=day, month=month, year=year)} является {Decimal(rub.replace(',', '.'))}"

print(currency_rate('USD'))
print(currency_rate('EUR'))
print(currency_rate('AUD'))