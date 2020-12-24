print("Hello world")

import config
import requests
import json

user = config.REDDITUSER
endpoint_list = ['hot','new','rising','top']
headers = { 'User-Agent' : user }
payload = {'g': 'GLOBAL', 'count': '100', 'limit': '100'}


substring_list = ['takeoff', 'moon', u"\U0001F680", u"\uE11D", u"\uE04C", 'gang', 'calls', 'thank you', 'tendies', 'yolo', 'bought', 'short squeeze', 'squeeze', 'tendy', 'tendie', 'thanks', '']

def scrapeReddit():
    matches = {}
    count = 0

    for x in endpoint_list:
        endpoint = 'https://www.reddit.com/r/wallstreetbets/{}.json'.format(x)
        r = requests.get(endpoint, headers=headers, params=payload).json()
        for x in r['data']['children']:
            temp = '{}{}'.format(x['data']['title'], x['data']['selftext'])

            if any( y in temp for y in substring_list ):
                count += 1
                formatData = {
                'title' : x['data']['title'],
                # 'text' : x['data']['selftext']
                'ups' : x['data']['ups'],
                'upvote_ratio' : x['data']['upvote_ratio'],
                'score' : x['data']['score'],
                'comment_count' : x['data']['num_comments']
                }
                matches[x['data']['name']] = (formatData)

    print(matches, count)

scrapeReddit()