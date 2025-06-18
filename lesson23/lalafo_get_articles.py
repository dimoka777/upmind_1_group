import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
from openpyxl import Workbook
from openpyxl.styles import Font


def parse_lalafo_article(article):
    """Parse individual article element and extract data"""
    data = {}

    # Title and URL
    title_elem = article.find('a', class_='lf-ad-tile__link')
    if title_elem:
        data['Title'] = title_elem.text.strip()
        data['URL'] = urljoin("https://lalafo.kg", title_elem['href'])

    # Price (main and USD)
    price_elem = article.find('p', class_='LFSubHeading')
    if price_elem:
        data['Price (KGS)'] = price_elem.text.strip()

    usd_elem = article.find('span', class_='LFCaption')
    if usd_elem:
        data['Price (USD)'] = usd_elem.text.strip()

    # Description
    desc_elem = article.find('span', class_='undercover-description')
    if desc_elem:
        data['Description'] = desc_elem.text.strip()

    # Image URL
    img_elem = article.find('img')
    if img_elem and 'src' in img_elem.attrs:
        data['Image URL'] = img_elem['src']

    # Seller info
    seller_elem = article.find('span', class_='userName-text')
    if seller_elem:
        data['Seller'] = seller_elem.text.strip()

    pro_label = article.find('span', class_='pro-label')
    data['PRO Seller'] = 'Yes' if pro_label else 'No'

    return data


def save_to_excel(data, filename):
    """Save scraped data to Excel file with formatting"""
    wb = Workbook()
    ws = wb.active
    ws.title = "Lalafo Listings"

    # Write headers
    headers = list(data[0].keys())
    ws.append(headers)

    # Format headers
    for col in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col)
        cell.font = Font(bold=True)

    # Write data
    for item in data:
        ws.append([item.get(header, '') for header in headers])

    # Auto-adjust column widths
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2
        ws.column_dimensions[column_letter].width = adjusted_width

    wb.save(filename)
    print(f"Data successfully saved to {filename}")


def scrape_lalafo(url, output_file='lalafo_data.xlsx', pages=1):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    all_data = []

    for page in range(1, pages + 1):
        print(f"Scraping page {page}...")
        page_url = f"{url}?page={page}" if page > 1 else url

        try:
            response = requests.get(page_url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.find_all('article', class_='lf-ad-tile')

            for article in articles:
                item_data = parse_lalafo_article(article)
                if item_data:
                    all_data.append(item_data)

            time.sleep(2)

        except Exception as e:
            print(f"Error scraping page {page}: {e}")
            continue

    if all_data:
        save_to_excel(all_data, output_file)

    return all_data


if __name__ == "__main__":
    data = scrape_lalafo(
        url="https://lalafo.kg",
        output_file="lalafo_listings.xlsx",
        pages=3
    )