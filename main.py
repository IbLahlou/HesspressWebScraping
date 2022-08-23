#Importation des Bibliothèque
from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font

#Creation d'un Fichier Excel avec les titres de chaque colonne
wb = Workbook()
ws = wb.active
ws.title = 'Posts'

heading = ['Title', 'Category', 'Date', 'Content', 'Link', 'Img']
ws.append(heading)

# Number of pages to scraping from Hespress
NUMBER_OF_PAGES = 6

print('[+] Start scraping Hespress')

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
}

# 29423 last page of Hesspress
for i in range(1, NUMBER_OF_PAGES):
    print(f'Filtrer les données de chaque page {str(i)} :')

    #Requesting
    html_text = requests.get('https://www.hespress.com/?action=ajax_listing&paged=' + str(i) +
                             '&tq=MjAyMi0wNC0wNiAwMDowNTowMA%3D%3D&all_listing=1', headers=headers).text

    #Parsing
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('div', class_='overlay card')

   