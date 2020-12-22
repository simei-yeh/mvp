print("Hello world")

import requests
import json

response = requests.get("https://www.reddit.com/r/wallstreetbets/hot.json")

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=2)
    print(text)

jprint(response.json())