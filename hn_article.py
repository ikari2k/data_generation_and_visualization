import requests
import json

url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"

response = requests.get(url=url)
print(f"status code: {response.status_code}")

response_dict = response.json()
print(json.dumps(response_dict, indent=4))
