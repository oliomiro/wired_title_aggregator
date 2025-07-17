from flask import Flask, render_template
import feedparser
from datetime import datetime
import html

app = Flask(__name__)

# List of Wired RSS feeds by category
RSS_FEEDS = [
    "https://www.wired.com/feed/rss",                      # main
    "https://www.wired.com/category/gear/rss",             # gear
    "https://www.wired.com/category/business/rss",         # business
    "https://www.wired.com/category/security/rss",         # security
    "https://www.wired.com/category/science/rss",          # science
    "https://www.wired.com/category/culture/rss",          # culture
    "https://www.wired.com/category/backchannel/rss",      # backchannel
]

CUTOFF_DATE = datetime(2022, 1, 1)

@app.route('/')
def index():
    articles = []
    seen_links = set()

    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            if not entry.get("published_parsed"):
                continue  # skip if no date available

            published = datetime(*entry.published_parsed[:6])
            if published < CUTOFF_DATE:
                continue

            title = html.unescape(entry.title)
            link = entry.link

            if link not in seen_links:
                articles.append({
                    'title': title,
                    'url': link,
                    'date': published
                })
                seen_links.add(link)

    # Sort by date, newest first
    articles.sort(key=lambda x: x['date'], reverse=True)

    return render_template("index.html", articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
