import requests


def get_currency_rate(currency, back=False):
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

    if back:
        return 1/(data['Valute'][currency]['Value']/data['Valute'][currency]['Nominal'])
    else:
        return data['Valute'][currency]['Value'] / data['Valute'][currency]['Nominal']