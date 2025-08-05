
import os
import requests
from datetime import datetime
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv()

PDS_URL = os.getenv("PDS_URL")
HANDLE = os.getenv("HANDLE")
PASSWORD = os.getenv("PASSWORD")

def login():
    url = f"{PDS_URL}/xrpc/com.atproto.server.createSession"
    payload = {"identifier": HANDLE, "password": PASSWORD}
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()["accessJwt"]

def fetch_posts(jwt):
    url = f"{PDS_URL}/xrpc/app.bsky.feed.getAuthorFeed?actor={HANDLE}&limit=100"
    headers = {"Authorization": f"Bearer {jwt}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json().get("feed", [])

def save_post_md(post):
    text = post["post"]["text"]
    if "#muja" not in text:
        return
    date = post["post"]["indexedAt"][:10]
    uri = post["post"]["uri"].split("/")[-1]
    slug = f"{date}_{uri}.md"
    with open(f"posts/{slug}", "w") as f:
        f.write(f"# Post del {date}\n\n")
        f.write(text)

if __name__ == "__main__":
    os.makedirs("posts", exist_ok=True)
    jwt = login()
    posts = fetch_posts(jwt)
    for post in posts:
        save_post_md(post)
