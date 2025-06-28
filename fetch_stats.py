import os
import requests
import json

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REFRESH_TOKEN = os.environ['REFRESH_TOKEN']
BLOG_ID = os.environ['BLOG_ID']

res = requests.post("https://oauth2.googleapis.com/token", data={
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'refresh_token': REFRESH_TOKEN,
    'grant_type': 'refresh_token'
})
access_token = res.json().get("access_token")

if not access_token:
    raise Exception("Failed to refresh access token")

resp = requests.get(
    f'https://blogger.googleapis.com/v3/blogs/{BLOG_ID}/pageviews?range=all',
    headers={'Authorization': f'Bearer {access_token}'}
)

if resp.status_code != 200:
    raise Exception("Failed to fetch data")

data = resp.json()
view_count = data['counts'][0]['count']

result = {
    'pageViews': view_count
}

json_path = 'data/stats.json'
os.makedirs(os.path.dirname(json_path), exist_ok=True)
with open(json_path, 'w') as f:
    json.dump(result, f, indent=2)
