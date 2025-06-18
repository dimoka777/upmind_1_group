import requests
from bs4 import BeautifulSoup


def scrape_website():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    data = []
    page_url = "https://lalafo.kg"

    response = requests.get(page_url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article', class_='lf-ad-tile')

    for article in articles:
        tmp = {}
        price = article.find('p', class_='LFSubHeading')
        if price:
            tmp['price'] = price.text.strip()

        title = article.find('a', class_='lf-ad-tile__link')
        if title:
            tmp['title'] = title.text.strip()

        img = article.find('img')
        if img:
            tmp['img'] = img.get('src')
        data.append(tmp)

    print(data)

if __name__ == "__main__":
    scrape_website()
