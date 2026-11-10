"""IS 310: Compare Wikipedia's MediaWiki Action API with Open Library."""

import json
import os
from pathlib import Path

import requests

WIKI_API = "https://en.wikipedia.org/w/api.php"
BOOK_API = "https://openlibrary.org/search.json"
TITLE = "One Thousand and One Nights"
FOLDER = Path(__file__).resolve().parent

CONTACT = os.getenv("API_CONTACT", "https://github.com/CultureAsData-UIUC/is310-fall-2026")
HEADERS = {"User-Agent": f"IS310CultureComparison/1.0 ({CONTACT})"}


def get_json(url, params):
    """Return decoded JSON, or None if the request fails."""
    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=20)
        if response.status_code != 200:
            print(f"Request failed: HTTP {response.status_code} ({url})")
            if response.status_code == 429:
                print("Rate limit reached. Retry later.")
            return None
        return response.json()
    except (requests.RequestException, ValueError) as error:
        print(f"Could not retrieve data from {url}: {error}")
        return None


def save_json(filename, items):
    path = FOLDER / filename
    with path.open("w", encoding="utf-8") as file:
        json.dump(items, file, indent=2, ensure_ascii=False)
    print(f"Saved: {path}")


def main():
    # 1. MediaWiki Action API: get the article's plain-text introduction.
    wiki = get_json(WIKI_API, {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": "1",
        "explaintext": "1",
        "redirects": "1",
        "titles": TITLE,
    })
    if wiki is not None:
        print("\nMEDIAWIKI RESPONSE:")
        print(json.dumps(wiki, indent=2, ensure_ascii=False))
        pages = wiki.get("query", {}).get("pages", {})
        wiki_items = [
            {
                "pageid": page.get("pageid"),
                "title": page.get("title"),
                "extract": page.get("extract", ""),
                "url": "https://en.wikipedia.org/wiki/" + page.get("title", "").replace(" ", "_"),
            }
            for page in pages.values() if "missing" not in page
        ]
        save_json("mediawiki_items.json", wiki_items)
    else:
        wiki_items = []

    # 2. Open Library API: search for books with the same title.
    books = get_json(BOOK_API, {
        "title": TITLE,
        "limit": 5,
        "fields": "key,title,author_name,first_publish_year,edition_count,language",
    })
    if books is not None:
        print("\nOPEN LIBRARY RESPONSE:")
        print(json.dumps(books, indent=2, ensure_ascii=False))
        book_items = [
            {
                "key": book.get("key"),
                "title": book.get("title"),
                "authors": book.get("author_name", []),
                "first_publish_year": book.get("first_publish_year"),
                "edition_count": book.get("edition_count"),
                "languages": book.get("language", []),
            }
            for book in books.get("docs", [])
        ]
        save_json("openlibrary_items.json", book_items)
    else:
        book_items = []

    # 3. Connect them by looking for the Wikipedia article title in book records.
    if wiki_items and book_items:
        wiki_title = wiki_items[0]["title"]
        matches = [book for book in book_items if book["title"].casefold() == wiki_title.casefold()]
        print("\nCONNECTION:")
        if matches:
            print(f"Found {len(matches)} exact title match(es) for '{wiki_title}'.")
            for match in matches:
                print(f"  {match['title']} - {match['key']}")
        else:
            print("No exact title match. Alternative titles or translations may explain this.")
            print("Open Library returned:", [book["title"] for book in book_items])
    else:
        print("\nCould not compare the two APIs because one returned no items.")


if __name__ == "__main__":
    main()
