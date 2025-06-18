import random
import time
import requests
from bs4 import BeautifulSoup


def parse_lalafo_advanced(url, pages=1, delay=1, proxies=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    session = requests.Session()
    if proxies:
        session.proxies.update(proxies)

    all_items = []

    for page in range(1, pages + 1):
        try:
            print(f"Parsing page {page}...")
            page_url = f"{url}?page={page}" if page > 1 else url

            # Random delay to avoid blocking
            time.sleep(delay + random.uniform(0, 1))

            response = session.get(page_url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.find_all('article', class_='adTile-wrap')

            for item in items:
                # Add your parsing logic here
                pass

        except Exception as e:
            print(f"Error on page {page}: {str(e)}")
            continue

    return all_items