import requests
import json
import time
import os
import re
from datetime import datetime

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"

ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {"User-Agent": "TrendPulse/1.0"}

CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

def get_category(title):
    title_lower = title.lower()
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in title_lower:
                return category
            
    return None

def clean_title(title):
    
    return re.sub(r"[^a-zA-Z0-9\s]", "", title)

def main():
    
    print("Fetching top stories...")

    try:
        response = requests.get(TOP_STORIES_URL, headers=headers)
        story_ids = response.json()[:500]
        print(f"Fetched {len(story_ids)} story IDs")
        
    except Exception as e:
        print("Failed to fetch top stories:", e)
        
        return

    collected_stories = []

    for category in CATEGORIES.keys():
        
        print(f"\nProcessing category: {category}")

        count = 0

        for i, story_id in enumerate(story_ids):
            
            if count >= 25:
                break

            try:
                res = requests.get(ITEM_URL.format(story_id), headers=headers)
                story = res.json()
            except Exception as e:
                print(f"Error fetching story {story_id}: {e}")
                continue

            if not story or "title" not in story:
                continue

            title = clean_title(story["title"])
            
            assigned_category = get_category(title)

            if assigned_category == category:
                
                print(f"[{category}] {count+1} -> {title[:60]}")

                collected_stories.append({
                    "post_id": story.get("id"),
                    "title": title,
                    "category": category,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by"),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })

                count += 1

            if i % 50 == 0:
                
                print(f"Checked {i} stories for {category}")

        print(f"Finished {category}: {count}")

        time.sleep(2)

    if not os.path.exists("data"):
        
        os.makedirs("data")

    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        
        json.dump(collected_stories, f, indent=4)

    print("\nDone")
    
    print(f"Collected {len(collected_stories)} stories")
    
    print(f"Saved to {filename}")

if __name__ == "__main__":
    main()