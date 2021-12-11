import requests
from bs4 import BeautifulSoup

URL = "https://www.idealista.com/alquiler-viviendas/cantabria/area-de-santander/con-precio-hasta_550/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print(soup)