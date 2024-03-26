## tristan_nouzille_projet2

# Scraping de données de livres

Ce script Python permet de scraper les données de livres à partir du site "Books to Scrape" (https://books.toscrape.com/) et de les sauvegarder dans un fichier CSV. Les données scrapées comprennent l'URL de la page du produit, le code UPC, le titre du livre, les prix (taxe incluse et taxe excluse), la quantité disponible, la description du produit, la catégorie, le classement des critiques, l'URL de l'image et le chemin de l'image téléchargée.

## Installation

1. Assurez-vous d'avoir Python installé sur votre système. Vous pouvez le télécharger à partir de [python.org](https://www.python.org/).

2. Clonez ce dépôt Git sur votre ordinateur :

'''bash
git clone 'https://github.com/tristan-nouzille/tristan_nouzille_projet2'
'''

3. Accédez au répertoire du projet avec la ligne de commande suivante :

'''bash

cd tristan_nouzille_projet2
'''

4. Créez un environnement virtuel pour isoler les dépendances (bibliothèque) du projet :

 1) Tout d'abord installez le package virtualenv avec la commande suivante dans votre terminal:
    '''bash
    $ pip install virtualenv
    '''
 2) créez votre environnement virtuel avec :
    
    '''bash
     $ virtualenv env
    '''
    Avec cette commande un dossier du nom de "env" apparaîtra dans votre projet 
 
5. Activez votre environnement, pour pouvoir l'utilisé il faut taper:

  '''bash
   $ source env/Scripts/activate
  '''
   Et si vous êtes sur Linux ou autre OS
    
   '''bash
   $ source env/bin/activate
   '''
   **Remarque :** "Scripts" commence avec un "S" majuscule, faite bien attention à cela.

    Quand ce dernier sera activé le nom apparaitra entre parenthèse en début de ligne sur votre terminal.
    Pour plus d'info, allez sur le lien suivant ' https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html '

## Dépendances

Ce projet utilise les bibliothèques Python suivantes :
- `requests` pour effectuer des requêtes HTTP
- `BeautifulSoup` pour le scraping HTML

Assurez-vous d'avoir installé ces bibliothèques en exécutant la commande d'installation des dépendances mentionnée ci-dessus.
Si ce n'est pas le cas, taper simplement la ligne suivante:

'''bash
 $ pip install requests
'''
et
'''bash
 $ pip install BeautifulSoup
'''


7. Exécutez le script principal pour scraper les données de livres et les sauvegarder dans un fichier CSV :

   ```bash
   python main.py
   ```
   Les données seront sauvegardées dans un fichier nommé "book_to_scrape_data.csv" dans le répertoire du projet.

8. Une fois que vous avez terminé d'utiliser le script, vous pouvez désactiver l'environnement virtuel en utilisant la commande suivante :

   ```bash
   deactivate
   ```

   
## Utilisation

1. Exécutez le script principal pour scraper les données de livres et les sauvegarder dans un fichier CSV :

 '''bash 
  $ python main.py
 '''


Les données seront sauvegardées dans un fichier nommé "book_to_scrape_data.csv" dans le répertoire du projet.

2. Une fois que vous avez terminé d'utiliser le script, vous pouvez désactiver l'environnement virtuel en utilisant la commande suivante :

- Sur Windows :
  ```
  deactivate
  ```

- Sur macOS et Linux :
  ```
  source venv/bin/deactivate
  ```

## Demo 

1. Pour une démonstration du projet, tapez :

'''bash
 $ python demo.py
'''
2. Choisissez la page que vous voulez scrapper depuis votre terminal (1, ...., 50)

3. Les données de la page sélectionée seront sauvegardées dans un fichier nommé "book_to_scrape_data.csv" dans le répertoire du projet.

4. Une fois que vous avez terminé d'utiliser le script demo.py, vous pouvez désactiver l'environnement virtuel en utilisant la commande suivante :

- Sur Windows :
  ```
  deactivate
  ```

- Sur macOS et Linux :
  ```
  source venv/bin/deactivate

---


