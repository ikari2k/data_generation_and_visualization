import requests
import json

# Send request to GH API
url = "https://api.github.com/rate_limit"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers)
print(f"Status code: {r.status_code}")

# Convert response to dictionary
response_dict = r.json()
readable = json.dumps(response_dict, indent=4)
print(readable)
