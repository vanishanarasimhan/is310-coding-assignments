# Supernatural Creatures in Tolkien's World

## My question
How do dragons and Maiar compare in how much information is documented about them on Tolkien Gateway?

## Why I chose this wiki
I chose [Tolkien Gateway](https://tolkiengateway.net/) because I am interested in folklore, fantasy, and supernatural creatures. Tolkien's stories include many kinds of beings, so I wanted to compare how the wiki describes two groups. This could help researchers explore how fans organize and document different parts of a fictional world.

## What I scraped
My `wiki_scraping.py` script starts at the [Dragons category](https://tolkiengateway.net/wiki/Category:Dragons) and the [Maiar category](https://tolkiengateway.net/wiki/Category:Maiar). It collects up to six article links from each category, then visits the individual articles. It saves the creature's name, category, URL, word count, number of internal links, and number of unique internal links in `creatures.csv`.

## Scraping policies and ethics
I checked [Tolkien Gateway's robots.txt](https://tolkiengateway.net/robots.txt). It blocks a number of named crawlers and warns against excessive automated traffic, but does not list a blanket `User-agent: *` prohibition. This is not unlimited permission. My script checks the rules for its own User-Agent, waits two seconds between requests, limits the number of pages, and skips blocked or unsuccessful responses. I also reviewed the [copyright page](https://tolkiengateway.net/wiki/Tolkien_Gateway:Copyrights), which states that site content is generally CC BY-SA 4.0, with separate rights for some images. I only save brief measurements and links, not images or full articles. I will check the site's current terms/community policies before running.

## How to run
In the `web-scraping` folder, install the packages:

```bash
python -m pip install requests beautifulsoup4
```

Replace `YOUR_NETID` in `wiki_scraping.py` with your own Illinois NetID, then run:

```bash
python wiki_scraping.py
```

If site access works, this creates `creatures.csv` in this folder.

## Reflection
The word and link counts show how much information wiki editors have added to each article, but they do not directly measure how important or popular a creature is. Some creatures might have shorter pages because there is less source material about them, not because fans care less about them. The article structure also affects what gets counted, and my script only samples a few pages per category. It would be incorrect to say that one category is more popular just because its pages have more words or links.
