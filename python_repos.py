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

# Analyze repos
print(f"\nSome info about all repos from the list")
for repo_dict in repo_dicts:
    print(f'Name: {repo_dict["name"]}')
    print(f'Owner: {repo_dict["owner"]["login"]}')
    print(f'Stars: {repo_dict["stargazers_count"]}')
    print(f'Repo url: {repo_dict["html_url"]}')
    print(f'Created at: {repo_dict["created_at"]}')
    print(f'Updated at: {repo_dict["updated_at"]}')
    print(f'Description: {repo_dict["description"]}')
