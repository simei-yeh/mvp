print("Hello world")

import config
import requests
import json

token = config.COIN

endpoint = 'https://rest-sandbox.coinapi.io/v1/exchangerate/'
headers = { 'content-type': 'application/json', 'X-CoinAPI-Key' : token }
payload = { 'apikey': token, 'asset_id_base': 'BTC', 'asset_id_quote': 'ETH' }

response = requests.get(endpoint, headers=headers, params=payload)
print(response.url)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=2)
    print(text)

jprint(response.json())