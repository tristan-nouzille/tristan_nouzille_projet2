import os
import re
import requests
from bs4 import BeautifulSoup
import csv

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def download_image(image_url, title, directory='images'):
    clean_title = re.sub(r'\W+', '', title)
    image_filename = f"{directory}/{clean_title}.jpg"
    try:
        img_response = requests.get(image_url)
        img_response.raise_for_status()  # Vérifier si la requête a réussi
        with open(image_filename, 'wb') as img_file:
            img_file.write(img_response.content)
        return image_filename
    except requests.exceptions.RequestException as e:
        print(f"Une erreur est survenue lors du téléchargement de l'image: {e}")
        return None

def scrape_book_data(link):
    try:
        response = requests.get(link)
        response.raise_for_status()  # Vérifier si la requête a réussi
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find('h1').text.strip()
        category = soup.find('ul', {'class': 'breadcrumb'}).find_all('a')[-1].text.strip()
        table_rows = soup.find('table', {'class': 'table table-striped'}).find_all('tr')
        upc = table_rows[0].find('td').text.strip()
        review_rating = table_rows[-1].find('td').text.strip()
        product_description = table_rows[1].find('td').text.strip()
        price_including_tax = table_rows[3].find('td').text.strip().replace('Â', '')
        price_excluding_tax = table_rows[2].find('td').text.strip().replace('Â', '')
        number_available = table_rows[5].find('td').text.replace('In stock', '').replace('(', '').replace(')', '').strip()
        image_url = soup.find('div', {'class': 'item'}).find('img')['src'].replace('../../', "http://books.toscrape.com/")
        image_filename = download_image(image_url, title)
        if image_filename:
            return [link, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url, image_filename]
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Une erreur est survenue lors du scraping des données: {e}")
        return None

def main():
    create_directory('images')
    with open('book_to_scrape_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['product_page_url', 'universal_product_code', 'title', 'price_including_tax',
                         'price_excluding_tax', 'number_available', 'product_description', 'category',
                         'review_rating', 'image_url', 'image_path'])
        
        for i in range(1, 51):
            url = f'https://books.toscrape.com/catalogue/page-{i}.html'
            try:
                response = requests.get(url)
                response.raise_for_status()  # Vérifier si la requête a réussi
                soup = BeautifulSoup(response.text, 'html.parser')
                books = soup.findAll('h3')
                for book in books:
                    a = book.find('a')
                    link = 'https://books.toscrape.com/catalogue/' + a['href']
                    book_data = scrape_book_data(link)
                    if book_data:
                        writer.writerow(book_data)
                        print('Scraped:', book_data[2])
            except requests.exceptions.RequestException as e:
                print(f"Une erreur est survenue lors de l'accès à l'URL: {url}, erreur: {e}")

if __name__ == "__main__":
    main()





   