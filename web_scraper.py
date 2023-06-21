from bs4 import BeautifulSoup
import requests

URL = "http://www.example.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())