import requests
import scraper
import urllib.request
import time
from bs4 import BeautifulSoup

def metaScraper(categoryURL): 
    response = requests.get(categoryURL)
    print(response)

    soup = BeautifulSoup(response.text, 'html.parser')

    #print(soup)

    buttons = soup.findAll("a", {"class": "btn btn-ecra btn"})

    links = []
    for guide in buttons:
        links.append(guide['href'])
        
    bigDict = {}
    for link in links:
        bigDict.update(scraper(link))
    return(bigDict)

categoryURLs = ['https://www.ethicalconsumer.org/energy','https://www.ethicalconsumer.org/fashion-clothing',
'https://www.ethicalconsumer.org/fashion-clothing','https://www.ethicalconsumer.org/food-drink',
'https://www.ethicalconsumer.org/health-beauty','https://www.ethicalconsumer.org/home-garden',
'https://www.ethicalconsumer.org/money-finance','https://www.ethicalconsumer.org/retailers',
'https://www.ethicalconsumer.org/technology','https://www.ethicalconsumer.org/transport-travel']


massiveDict = {}
for url in categoryURLs:
    d = metaScraper(url)
    massiveDict.update(d)

with open('result.json', 'w') as fp:
    json.dump(bigDict, fp)