## tristan_nouzille_projet2

# Scraping de données de livres

Ce script Python permet de scraper les données de livres à partir du site "Books to Scrape" (https://books.toscrape.com/) et de les sauvegarder dans un fichier CSV. Les données scrapées comprennent l'URL de la page du produit, le code UPC, le titre du livre, les prix (taxe incluse et taxe excluse), la quantité disponible, la description du produit, la catégorie, le classement des critiques, l'URL de l'image et le chemin de l'image téléchargée.

## Installation

1. Assurez-vous d'avoir Python installé sur votre système. Vous pouvez le télécharger à partir de [python.org](https://www.python.org/).

2. Clonez ce dépôt Git sur votre ordinateur :

```
 git clone 'https://github.com/tristan-nouzille/tristan_nouzille_projet2'
```

3. Accédez au répertoire du projet avec la ligne de commande suivante :

```
 cd tristan_nouzille_projet2
```

4. Créez un environnement virtuel pour isoler les dépendances (bibliothèque) du projet :

  Pour plus d'info, allez sur le lien suivant ' https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html '

 ## Dépendances

 Ce projet utilise les bibliothèques Python présent dans le fichier requirement.txt.

 Installé ces bibliothèques en exécutant la commande suivante:

 ```
  pip install -r requirements.txt
 ```

   
## Utilisation

1. Exécutez le script principal pour scraper les données de livres et les sauvegarder dans un fichier CSV :

 ```
  python main.py
 ```
 et tapez 'main' quand l'application le demandera.


Les données seront sauvegardées dans un fichier nommé "book_to_scrape_data.csv" dans le répertoire du projet ainsi qu'un dossier images avec toutes les couvertures des livres.
Une fois terminé, désactivez l'environnement virtuel.

## Demo 

1. Pour une démonstration du projet, tapez :

```
 demo 
```
2. Choisissez la page que vous voulez scrapper depuis votre terminal (1, ...., 50)

3. Les données de la page sélectionée seront sauvegardées dans un fichier nommé "book_to_scrape_data.csv" dans le répertoire du projet.

4. Une fois que vous avez terminé d'utiliser le script demo.py, vous pouvez désactiver l'environnement virtuel

---


