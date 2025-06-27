import os
import requests
import json
from datetime import datetime

# 环境变量
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REFRESH_TOKEN = os.environ['REFRESH_TOKEN']
BLOG_ID = os.environ['BLOG_ID']

# 获取访问令牌
res = requests.post("https://oauth2.googleapis.com/token", data={
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'refresh_token': REFRESH_TOKEN,
    'grant_type': 'refresh_token'
})
access_token = res.json().get("access_token")
print("access_token", access_token )
if not access_token:
    raise Exception("Failed to refresh access token")

# 获取访问数据
resp = requests.get(
    f'https://blogger.googleapis.com/v3/blogs/{BLOG_ID}/pageviews?range=all',
    headers={'Authorization': f'Bearer {access_token}'}
)

print("Status Code:", resp.status_code)
print("Response Text:", resp.text)  # 打印原始内容（很关键）

if resp.status_code != 200:
    raise Exception("Failed to fetch data")

data = resp.json()

view_count = data['counts'][0]['count']

# 加载旧数据并追加
json_path = 'data/stats.json'
try:
    with open(json_path, 'r') as f:
        history = json.load(f)
except FileNotFoundError:
    history = []

history.append({
    'timestamp': datetime.utcnow().isoformat() + 'Z',
    'pageViews': view_count
})

# 保存新数据
with open(json_path, 'w') as f:
    json.dump(history, f, indent=2)
