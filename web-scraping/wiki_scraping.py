"""IS310: Compare documentation of Dragons and Maiar on Tolkien Gateway."""
import csv
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup

BASE = "https://tolkiengateway.net"
CATEGORIES = {
    "Dragons": f"{BASE}/wiki/Category:Dragons",
    "Maiar": f"{BASE}/wiki/Category:Maiar",
}

USER_AGENT = "is310-course-scraper/1.0 (student project; vnara3@illinois.edu)"
DELAY_SECONDS = 2
MAX_PER_CATEGORY = 6
OUTPUT = Path(__file__).with_name("creatures.csv")


def get_soup(url, robots, session):
    """Respect robots.txt and rate limits; skip blocked or failed pages."""
    if not robots.can_fetch(USER_AGENT, url):
        print("Blocked by robots.txt:", url)
        return None
    time.sleep(DELAY_SECONDS)
    try:
        response = session.get(url, timeout=15)
        print(response.status_code, url)
        if response.status_code != 200:
            return None
        if "text/html" not in response.headers.get("Content-Type", ""):
            return None
        if "Just a moment" in response.text[:1000]:
            print("Bot protection detected; not attempting to bypass it.")
            return None
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as error:
        print("Request failed:", error)
        return None


def get_category_pages(soup):
    """Find individual article links from a wiki category page."""
    category_area = soup.select_one("#mw-pages")
    if category_area is None:
        print("Could not locate the category page list.")
        return []
    pages = []
    seen = set()
    for a in category_area.select(".mw-category a, .mw-category-group a"):
        href = a.get("href", "")
        url = urljoin(BASE, href)
        path = urlparse(url).path
        if not path.startswith("/wiki/") or ":" in path[6:] or url in seen:
            continue
        seen.add(url)
        pages.append({"name": a.get_text(" ", strip=True), "url": url})
        if len(pages) >= MAX_PER_CATEGORY:
            break
    return pages


def analyze_article(soup, name, category, url):
    """Count article words and internal wiki links, not whole-page navigation."""
    content = soup.select_one("#mw-content-text .mw-parser-output")
    if content is None:
        content = soup.select_one("#mw-content-text")
    if content is None:
        print("Missing article content:", url)
        return None
    
    for node in content.select("script, style, .toc, .navbox, .mw-editsection"):
        node.decompose()
    words = len(content.get_text(" ", strip=True).split())
    links = [a.get("href", "") for a in content.select('a[href^="/wiki/"]')]
    links = [link for link in links if ":" not in link[len("/wiki/"):]]
    return {
        "name": name,
        "category": category,
        "article_url": url,
        "word_count": words,
        "internal_link_count": len(links),
        "unique_internal_link_count": len(set(links)),
    }


def main():

    robots = RobotFileParser()
    robots.set_url(f"{BASE}/robots.txt")
    try:
        robots.read()
        if robots.mtime() == 0:
            print("Could not verify robots.txt. Stopping.")
            return
    except Exception as error:
        print("Could not read robots.txt; stopping:", error)
        return

    records = []
    with requests.Session() as session:
        session.headers.update({"User-Agent": USER_AGENT})
        for category, url in CATEGORIES.items():
            soup = get_soup(url, robots, session)
            if soup is None:
                continue
            pages = get_category_pages(soup)
            print(f"Found {len(pages)} {category} article links")
            for page in pages:
                article_soup = get_soup(page["url"], robots, session)
                if article_soup is None:
                    continue
                result = analyze_article(article_soup, page["name"], category, page["url"])
                if result is not None:
                    records.append(result)

    if not records:
        print("No data collected. Check access, selectors, and site policies.")
        return
    with OUTPUT.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    print(f"Saved {len(records)} records to {OUTPUT}")
    for category in CATEGORIES:
        counts = [row["word_count"] for row in records if row["category"] == category]
        if counts:
            print(f"{category}: {len(counts)} pages, average {sum(counts)/len(counts):.0f} words")


if __name__ == "__main__":
    main()