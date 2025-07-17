# Wired Title Aggregator

This project is a backend assessment submission that builds a **title aggregator** for articles from [Wired.com](https://www.wired.com). It scrapes article titles, URLs, and publish dates from multiple official Wired RSS feeds and displays them on a simple, black-and-white Flask website.

## ✅ Features

- Collects articles from **multiple Wired RSS feeds**
- Filters articles published **on or after 1 January 2022**
- Sorts titles in **reverse chronological order**
- Displays **publish dates** for clarity
- Each title is a clickable hyperlink to the original article
- Clean black-and-white UI (no images or videos)

## 📰 Data Sources

This aggregator uses the following public RSS feeds:

- https://www.wired.com/feed/rss
- https://www.wired.com/category/gear/rss
- https://www.wired.com/category/business/rss
- https://www.wired.com/category/security/rss
- https://www.wired.com/category/science/rss
- https://www.wired.com/category/culture/rss
- https://www.wired.com/category/backchannel/rss

> ⚠ Note: Each RSS feed is limited to ~20–30 recent articles. Due to Wired’s feed structure and deprecation of full archives, only the latest posts are available (even after filtering by publish date).

## 🛠 Tech Stack

- Python 3
- Flask
- feedparser
- HTML / CSS (minimal styling)

## 🚀 Run Locally

```bash
# Clone this repo
cd wired_aggregator

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
