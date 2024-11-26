# Email Scraper and Link Crawler

This Python script scrapes email addresses and crawls through links from a given URL. It collects emails from the pages it crawls and stores them in a set. It follows links on each page, discovering and scraping new pages recursively (up to a specified limit).

## Features

- Scrapes email addresses from the provided URL.
- Crawls through internal links within the site.
- Follows both relative and absolute links.
- Collects unique emails and prints them at the end.
- Allows setting a crawl limit for the number of pages to be processed.

## Requirements

To run the script, you need Python 3.x and the following libraries:

- `requests`
- `beautifulsoup4`

You can install the required libraries using `pip`:

```bash
pip install requests beautifulsoup4
```

## How to Use

1. Clone the repository or download the script to your local machine.
2. Open a terminal and navigate to the folder containing the script.
3. Run the script using Python:

   ```bash
   python email_scraper.py
   ```

4. The script will prompt you to enter a URL and a search limit.
   - **URL**: The starting point URL for crawling.
   - **Search Limit**: The maximum number of pages to crawl.

5. The script will process the pages, extract email addresses, and follow links up to the specified search limit.

6. After completing the crawl, it will display the found email addresses.

## Example Usage

```bash
[+] Enter Url: https://example.com
[+] Enter search limit: 5
1 Processing https://example.com
2 Processing https://example.com/about
3 Processing https://example.com/contact
...

Process Done!

3 email(s) ditemukan

  user@example.com
  contact@example.org
  info@example.net
```

## Code Explanation

- **URL Input**: The script prompts the user to input a starting URL and a search limit (number of pages to crawl).
- **Crawling and Scraping**: The script uses a queue (`deque`) to store URLs to be crawled and a set to track scraped URLs to avoid revisiting them. It uses the `requests` library to fetch page content and `BeautifulSoup` to parse the HTML.
- **Email Extraction**: Emails are extracted using a regular expression (`re.findall`) and stored in a set to ensure uniqueness.
- **Link Following**: The script follows both relative and absolute links. Relative links are converted to full URLs using `urllib.parse.urljoin`.

## Error Handling

- **Timeout and Connection Errors**: The script will handle common network-related errors, such as connection errors or timeouts, and will skip URLs that are not reachable.
- **Invalid Input**: The script checks that the search limit is a valid positive integer.
