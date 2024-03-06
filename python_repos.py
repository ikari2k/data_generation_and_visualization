import requests

# Send request to GH API
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers)
print(f"Status code: {r.status_code}")

# Convert response to dictionary
response_dict = r.json()

# Process the results
print(response_dict.keys())
