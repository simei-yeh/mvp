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

substring_list = ['takeoff', 'moon', u"\U0001F680", u"\uE11D", 'gang', 'calls', 'thank you', 'tendies', 'yolo', 'bought', 'short squeeze', 'squeeze', 'tendy', 'tendie', 'thanks']

def jprint(obj):
    matches = []
    count = 0
    for x in obj['data']['children']:
        count += 1
        if any( y in x['data']['title'] for y in substring_list):
            matches.append(x['data']['name'])
        print(x['data']['title'])
        print(x['data']['selftext'])
    print(matches, count)

jprint(response.json())