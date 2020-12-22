print("Hello world")

import config
import requests
import json

user = config.REDDITUSER
endpoint = 'https://www.reddit.com/r/wallstreetbets/hot.json'
headers = { 'User-Agent' : user }
payload = {'g': 'GLOBAL', 'count': '100', 'limit': '100'}


response = requests.get(endpoint, headers=headers, params=payload)
print(response.url)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=2)
    print(text)

jprint(response.json())