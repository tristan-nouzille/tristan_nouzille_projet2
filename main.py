import os
import re
import requests
from bs4 import BeautifulSoup
import csv
import time

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
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find('h1').text.strip()
        category = soup.find('ul', {'class': 'breadcrumb'}).find_all('a')[-1].text.strip()
        rows = soup.find('table', {'class': 'table table-striped'}).find_all('tr')
        upc = rows[0].find('td').text.strip()
        price_including_tax = rows[3].find('td').text.replace('Â', '')
        price_excluding_tax = rows[2].find('td').text.replace('Â', '')
        
        # Correction pour récupérer le nombre de livres disponibles
        number_available_raw = rows[5].find('td').text.strip()  
        number_available_match = re.search(r'\d+', number_available_raw)
        if number_available_match:
            number_available = number_available_match.group()
        else:
            number_available = "N/A"  
        review_mapping = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }
        review_p = soup.find('p', class_='star-rating')
        if review_p:
            review_rating_text = review_p['class'][1] 
            review_rating = review_mapping.get(review_rating_text, 0)  
        else:
            review_rating = 0  
        
        product_description = soup.find('meta', attrs={'name': 'description'})['content']
        product_description = re.sub(r'[^a-zA-Z0-9\s.,]', '', product_description)
        
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
        
        page_number = 1
        while True:
            url = f'https://books.toscrape.com/catalogue/page-{page_number}.html'
            try:
                response = requests.get(url)
                if response.status_code == 404:
                    print("Page non trouvée. Arrêt du scraping.")
                    break
                
                response.raise_for_status()  # Vérifier si la requête a réussi
                soup = BeautifulSoup(response.text, 'html.parser')
                books = soup.findAll('h3')
                if not books:  # Si aucun livre n'est trouvé, arrêter la boucle
                    break
                for book in books:
                    a = book.find('a')
                    link = 'https://books.toscrape.com/catalogue/' + a['href']
                    book_data = scrape_book_data(link)
                    if book_data:
                        writer.writerow(book_data)
                        print('Scraped:', book_data[2])
                
                # Pause de 2 secondes entre chaque requête
                time.sleep(2)
            
            except requests.exceptions.RequestException as e:
                print(f"Une erreur est survenue lors de l'accès à l'URL: {url}, erreur: {e}")
            
            page_number += 1
            
        print("Scraping terminé.")

if __name__ == "__main__":
    main()
