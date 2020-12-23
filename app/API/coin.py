print("Hello world")

import config
import requests
import json

token = config.COIN

asset_id_base = 'BTC'
asset_id_quote = 'USD'
endpoint = 'https://rest.coinapi.io/v1/exchangerate/{}/{}'.format(asset_id_base, asset_id_quote)
headers = { 'content-type': 'application/json', 'X-CoinAPI-Key' : token }
payload = { 'invert': 'false' }

response = requests.get(endpoint, headers=headers, params=payload)


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=2)
    json_data = json.loads(text)
    print(json_data)

jprint(response.json())