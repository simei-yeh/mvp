print("Hello world")

import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=2)
    print(text)

jprint(response.json())