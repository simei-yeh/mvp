print("Hello world")

import os
import sys
sys.path.append(os.path.realpath('.'))
from database.connect import insert
from external.tokens import COIN
import requests
import json
import threading

token = COIN

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

    # organize data into csv file
    for x in r['rates']:
        x['asset_id_base'] = "USD"
        data = json.dumps(x)
        query = "INSERT INTO vol.crypto (time,asset_id_base,asset_id_quote,rate)  \
            SELECT time,asset_id_base,asset_id_quote,rate FROM json_populate_record (NULL::vol.crypto,'{}')".format(data, data)

        res = insert(query)

    # copy data into database
    print(len(r['rates']))

if __name__ == "__main__":
    coinQuotes()
# setInterval(coinQuotes, 120)