import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.ethicalconsumer.org/food-drink'
response = requests.get(url)
print(response)

soup = BeautifulSoup(response.text, 'html.parser')

#print(soup)

buttons = soup.findAll("a", {"class": "btn btn-ecra btn"})

links = []
for guide in buttons:
    links.append(guide['href'])