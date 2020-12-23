print("Hello world")

import config
import requests
import json

token = config.COIN

asset_id_base = 'USD'
asset_id_quote = ''
endpoint = 'https://rest.coinapi.io/v1/exchangerate/{}/{}'.format(asset_id_base, asset_id_quote)
headers = { 'content-type': 'application/json', 'X-CoinAPI-Key' : token }
payload = { 'invert': 'true' }

response = requests.get(endpoint, headers=headers, params=payload)


def jprint(obj):
    # create a formatted string of the Python JSON object
    formattedData = []

    for x in obj['rates']:
        x['asset_id_base'] = 'USD'
        formattedData.append(x.copy())

    text = json.dumps(formattedData, sort_keys=True, indent=2)

    with open('formattedCoin.json', 'w') as ftd:
        ftd.write(text)


jprint(response.json())