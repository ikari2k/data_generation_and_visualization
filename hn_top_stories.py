import requests
from operator import itemgetter

url = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(url=url)
print(f"status code: {response.status_code}")

submission_ids = response.json()
submission_dicts = []

for submission_id in submission_ids[:10]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    submission_dict = {
        "title": response_dict["title"],
        "hn_link": f"http://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict["descendants"],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

for submission in submission_dicts:
    print(f'\n Article name: {submission["title"]}')
    print(f'Article name link: {submission["hn_link"]}')
    print(f'No of comments: {submission["comments"]}')
