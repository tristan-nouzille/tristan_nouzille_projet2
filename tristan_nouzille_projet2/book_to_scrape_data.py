import requests
from bs4 import BeautifulSoup
import csv

links = []

# Parcourir les pages pour obtenir les liens des livres
for i in range(1, 51):
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    response = requests.get(url)
    
    if response.ok:
        print('Page:', i)
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.findAll('h3')
        for book in books:
            a = book.find('a')
            link = 'https://books.toscrape.com/catalogue/' + a['href']
            links.append(link)

# Écrire dans le fichier CSV en dehors de la boucle de parcours des pages
with open('book_to_scrape_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['product_page_url', 'universal_ product_code', 'title','price_including_tax', 'price_excluding_tax', 
                         'number_available','product_description', 'category', 'review_rating', 'image_url'])  # En-tête du fichier CSV
    
    # Parcourir les liens des livres pour obtenir les données de chaque livre
    for link in links:
        response_book = requests.get(link)
        if response_book.ok:
            soup_book = BeautifulSoup(response_book.text, "html.parser")
            title = soup_book.find('h1').text.strip()
            breadcrumbs = soup_book.find('ul', {'class': 'breadcrumb'})
            category = breadcrumbs.find_all('a')[-1].text.strip()
            meta_description = soup_book.find('meta', {'name': 'description'})['content'].replace('â', '"').strip()
            table = soup_book.find('table', {'class': 'table table-striped'})
            rows = table.find_all('tr')
            upc = rows[0].find('td').text.strip()
            price_including_tax = rows[3].find('td').text.strip().replace('Â', '')
            price_excluding_tax = rows[2].find('td').text.strip().replace('Â', '')
            number_available = rows[5].find('td').text.replace('In stock', '').replace('(', '').replace(')', '')
            review_rating = rows[6].find('td').text.strip()
            product_description = rows[1].find('td',).text.strip()
            image_url = soup_book.find('div', {'class' : 'item active'}).find('img')['src'].replace('../../', "http://books.toscrape.com/")
            
            writer.writerow([link, upc, title, price_including_tax, price_excluding_tax, number_available,product_description, category, review_rating, image_url ])

print('Données enregistrées.')

   