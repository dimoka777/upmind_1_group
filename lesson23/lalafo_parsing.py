import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin


def parse_lalafo(url, pages=1, output_file='lalafo_items.csv'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    all_items = []

    for page in range(1, pages + 1):
        print(f"Parsing page {page}...")
        page_url = f"{url}?page={page}" if page > 1 else url
        response = requests.get(page_url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to fetch page {page}. Status code: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('article', class_='adTile-wrap')  # Update class if needed

        for item in items:
            title_elem = item.find('a', class_='adTile-title')
            price_elem = item.find('p', class_='adTile-price')
            location_elem = item.find('div', class_='adTile-location')

            if not title_elem:
                continue

            title = title_elem.text.strip()
            link = urljoin(url, title_elem['href'])
            price = price_elem.text.strip() if price_elem else "Цена не указана"
            location = location_elem.text.strip() if location_elem else "Местоположение не указано"

            all_items.append({
                'title': title,
                'price': price,
                'location': location,
                'link': link
            })

    # Save to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'price', 'location', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_items)

    print(f"Successfully parsed {len(all_items)} items. Saved to {output_file}")


# Example usage
if __name__ == "__main__":
    parse_lalafo("https://lalafo.kg/kyrgyzstan", pages=3)