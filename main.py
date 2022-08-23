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