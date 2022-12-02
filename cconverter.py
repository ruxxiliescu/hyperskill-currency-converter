import requests
import json

currencies = {}
for i in ['usd', 'eur']:
    r = requests.get("http://www.floatrates.com/daily/" + i + ".json")
    currencies[i] = json.loads(r.text)

currency_code = input().lower()

while True:
    exchange_currency = input().lower()
    if exchange_currency == "":
        exit()
    amount = float(input())
    print('Checking the cache... ')
    if exchange_currency in currencies.keys():
        print('Oh! It is in the cache!')
        exchanged = amount / currencies[exchange_currency][currency_code]['rate']
        new_currency = exchange_currency.upper()
        print(f'You received {round(exchanged,2)} {new_currency}.')
    else:
        print('Sorry, but it is not in the cache!')
        r = requests.get("http://www.floatrates.com/daily/" + exchange_currency + ".json")
        fx = json.loads(r.text)
        exchanged = amount / fx[currency_code]['rate']
        new_currency = exchange_currency.upper()
        print(f"You received {round(exchanged,2)} {new_currency}.")
        currencies[exchange_currency] = fx
