print("Hello world")

from connect import connect
import requests
import json

endpoint="https://localhost:5000/v1/api/iserver/secdef/strikes"
headers = { 'content-type': 'application/json;charset=utf-8' }
payload = { 'conid': '444857009', 'sectype':'OPT', 'month': 'JAN21'}

ticker_list= ['GME', 'STIC', 'NIO', 'PLTR', 'TSLA', 'BABA', 'AAPL', 'DKNG', 'MT', 
'IPOC', 'FCEL', 'PENN', 'NKLA', 'ARK', 'QS', 'GILD', 'PSTH', 'MVIS', 'TLRY','MARA']

response = requests.get(endpoint, headers=headers, params=payload, verify=False)


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=2)
    json_data = json.loads(text)
    print(json_data)

jprint(response.json())