import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

def main():
    url = f"https://newsapi.org/v2/everything?q=india&sortBy=publishedAt&language=en&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])
    keywords = []
    for article in articles:
        if article.get("title"):
            keywords.append(article["title"])
    df = pd.DataFrame(keywords, columns=["keyword"])
    df.to_csv("raw_data.csv", index=False, encoding="utf-8")
    print("Data collected successfully")
    print(df.head())

if __name__ == "__main__":
    main()