# Getting Culture Across APIs

For this assignment, I used the Wikipedia MediaWiki Action API and the Open Library API. I chose *One Thousand and One Nights* because it connects to my project about jinn stories and folklore. I wanted to see how the same cultural work appears in two different types of collections.

## Running the script

Install `requests` if needed:

```bash
python -m pip install requests
```

From this folder, run:

```bash
python getting_culture.py
```

The script prints the API responses, compares the title across both services, and saves only selected item fields in `mediawiki_items.json` and `openlibrary_items.json`. It checks HTTP status codes and handles errors without crashing. No API key is needed for these public queries. You can identify your requests with your own public contact URL or email using the `API_CONTACT` environment variable.

## Comparing the APIs

Wikipedia's MediaWiki API and Open Library both provide cultural information, but they organize it differently. MediaWiki gives me an encyclopedia article about *One Thousand and One Nights*, while Open Library gives me structured book records, such as titles, authors, publication years, languages, and edition counts. Both can be used without a private key for these requests, but they ask users to identify their scripts with a User-Agent. Open Library also encourages people to register their applications. Open Library lists a limit of one request per second for unidentified requests and three per second for properly identified requests. Wikimedia uses different rate limits depending on how the client is identified, and it asks developers to respect throttling responses. Wikipedia is operated by the nonprofit Wikimedia Foundation, while Open Library is a project of the nonprofit Internet Archive. These projects depend on continued support and maintenance, so access could change in the future. The two APIs also show different gaps. Wikipedia depends on which stories contributors have written about, while Open Library depends on which books and editions have been cataloged. Stories passed down orally, or stories without widely published editions, may be harder to find. This matters for my jinn project because folklore does not always fit into a single article or book record. Both APIs are useful for research, but their formats were not made specifically to compare cultural storytelling across communities.

## Connecting the results

I took the Wikipedia article title, *One Thousand and One Nights*, and used that title to search Open Library. The script checks for exact title matches and prints what it finds. Even when the title matches, it does not necessarily mean the records describe the same version or translation. If there is no exact match, the script prints the alternative book titles so I can see the problem instead of treating it as a failed assignment.

**After running:** Add one sentence here with your actual result (for example, the title of a matched Open Library record and whether it refers to a specific edition).

## Sources

- [MediaWiki Action API etiquette](https://www.mediawiki.org/wiki/API:Etiquette)
- [Wikimedia API rate limits](https://www.mediawiki.org/wiki/Wikimedia_APIs/Rate_limits)
- [Open Library API documentation and rate limits](https://openlibrary.org/developers/api)
- [Open Library search API documentation](https://openlibrary.org/dev/docs/api/search)
