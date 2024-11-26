from collections import deque
import re
from bs4 import BeautifulSoup
import requests
import urllib.parse

user_url = str(input('[+] Enter Url: '))
urls = deque([user_url])
scraped_urls = set()
emails = set()
count = 0
limit = int(input('[+] Enter search limit: '))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    while urls:
        count += 1
        if count > limit:
            break

        url = urls.popleft()
        if url in scraped_urls:
            continue
        scraped_urls.add(url)
        
        parts = urllib.parse.urlsplit(url)
        base_url = f'{parts.scheme}://{parts.netloc}'
        path = url[:url.rfind('/') + 1] if '/' in parts.path else url  

        print(f'{count} Processing {url}')

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise exception for bad responses
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.HTTPError):  
            continue

        new_emails = set(re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.-]+\.[a-z]{2,}', response.text, re.I))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, 'html.parser')

        for anchor in soup.find_all('a'):
            link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link

            if link not in urls and link not in scraped_urls:
                urls.append(link)

except KeyboardInterrupt:
    print('[-] Closing!')

print('\nProcess Done!')
print(f'\n{len(emails)} emails found\n')

for mail in emails:
    print('  ' + mail)
print('\n')
