print("Hello world")

from connect import connect
import tokens
import requests
import json
import threading

token = tokens.COIN

asset_id_base = 'USD'
asset_id_quote = ''
endpoint = 'https://rest.coinapi.io/v1/exchangerate/{}/{}'.format(asset_id_base, asset_id_quote)
headers = { 'content-type': 'application/json', 'X-CoinAPI-Key' : token }
payload = { 'invert': 'true' }

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()
        print('done with interval request')

def coinQuotes():
    #send request to server
    r = (requests.get(endpoint, headers=headers, params=payload)).json()
    print(r)
    # organize data into csv file
    for x in r['rates']:
        with open('formattedCoin.csv', 'a') as ftdC:
            ftdC.write('USD,{},{},{}\n'.format(x['asset_id_quote'],x['rate'],x['time']) )

    # copy data into database
    print('done with current request')


coinQuotes()
# setInterval(coinQuotes, 120)