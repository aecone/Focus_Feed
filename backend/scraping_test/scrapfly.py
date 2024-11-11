import json
from urllib.parse import quote
import jmespath
from typing import Dict
from datetime import datetime, timezone
from backend.app.config import get_db_connection
from scrapfly import ScrapflyClient, ScrapeConfig
from dotenv import load_dotenv
import os
load_dotenv(os.path.join(os.path.dirname(__file__), '../local.env'))

# Initialize Scrapfly client with your API key
SCRAPFLY = ScrapflyClient(key=os.getenv("SCRAPFLY_KEY"))

def parse_post(data: Dict) -> Dict:
    print(f"Parsing post data {data.get('shortcode', 'N/A')}")
    result = jmespath.search("""
    {
        id: id,
        shortcode: shortcode,
        dimensions: dimensions,
        src: display_url,
        src_attached: edge_sidecar_to_children.edges[].node.display_url,
        video_url: video_url,
        location: location.name,
        taken_at: taken_at_timestamp,
        is_video: is_video,
        tagged_users: edge_media_to_tagged_user.edges[].node.user.username,
        captions: edge_media_to_caption.edges[].node.text
    }
    """, data)

    if result and 'taken_at' in result:
        # Convert taken_at_timestamp to a readable format
        result['taken_at'] = datetime.fromtimestamp(result['taken_at'], tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

    if result:
        result['link'] = f"https://www.instagram.com/p/{result['shortcode']}/"
        return result
    else:
        print(f"Failed to parse post data for shortcode: {data.get('shortcode', 'N/A')}")
        return {}

# Helper function to scrape user posts using Scrapfly
def scrape_user_posts(user_id: str, page_size=12, max_pages: int = None):
    base_url = "https://www.instagram.com/graphql/query/?query_hash=e769aa130647d2354c40ea6a439bfc08&variables="
    variables = {
        "id": user_id,
        "first": page_size,
        "after": None,
    }
    _page_number = 1
    while True:
        url = base_url + quote(json.dumps(variables))
        result = SCRAPFLY.scrape(ScrapeConfig(url=url, asp=True))
        
        data = json.loads(result.content)
        posts = data["data"]["user"]["edge_owner_to_timeline_media"]
        for post in posts["edges"]:
            yield parse_post(post["node"])
        page_info = posts["page_info"]
        
        if _page_number == 1:
            print(f"Scraping total {posts['count']} posts of {user_id}")
        else:
            print(f"Scraping page {_page_number}")
        
        if not page_info["has_next_page"] or (max_pages and _page_number >= max_pages):
            break
        variables["after"] = page_info["end_cursor"]
        _page_number += 1

# Function to retrieve the user ID based on Instagram username using Scrapfly
def scrape_user(username: str):
    """Scrape Instagram user's data"""
    result = SCRAPFLY.scrape(ScrapeConfig(
        url=f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}",
        headers={
            "x-ig-app-id": "936619743392459",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "*/*",
        },
        asp=True
    ))
    data = json.loads(result.content)
    user_id = data["data"]["user"]['id']
    print(user_id)
    return user_id

def main():
    try:
        conn = get_db_connection()
        print("Connection successful")
        # Optionally, check the current database state, e.g., running a simple query
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            db_version = cur.fetchone()
            print(f"Database version: {db_version}")
    except Exception as e:
        print(f"Connection failed: {e}")
    finally:
        if conn:
            conn.close()
            print('Database connection closed')
    
    user_name = input("Enter the username: ")
    user_id = scrape_user(user_name)
    
    posts = list(scrape_user_posts(user_id, max_pages=3))
    print(json.dumps(posts, indent=2, ensure_ascii=False))

# Example run:
if __name__ == "__main__":
    main()
