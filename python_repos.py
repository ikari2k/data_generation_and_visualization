import requests

# Send request to GH API
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers)
print(f"Status code: {r.status_code}")

# Convert response to dictionary
response_dict = r.json()
print(f'Total number of repos: {response_dict["total_count"]}')
print(f'Complete result: {not response_dict["incomplete_results"]}')

# Process the results
repo_dicts = response_dict["items"]
print(f"Number of returned repos: {len(repo_dicts)}")

# Analyze first repo
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
