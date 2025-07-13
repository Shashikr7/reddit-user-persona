import os
import re

def extract_username(url):
    match = re.search(r"reddit.com/user/([^/]+)/?", url)
    return match.group(1) if match else None

def save_to_file(username, content):
    os.makedirs("output", exist_ok=True)
    with open(f"output/{username}.txt", "w", encoding="utf-8") as f:
        f.write(content)
