import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json

all_companies = {}
def sub_scraper(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    #print(soup)

    mydivs = soup.findAll("div", {"class": "product-company"})

    products = []
    companyNames = []
    for div in mydivs:
        products.append(div.contents[1].contents[0])
        fullText = div.getText()
        actual = fullText[fullText.find(':') + 2:]
        companyNames.append(actual)
        #companyNames.append(div.contents[1].contents[1])
        '''companyNames.append(div.contents[1].contents[1])'''

    #print(companyNames)
    
    good = soup.findAll("div", {"class": "score good"})
    average = soup.findAll("div", {"class": "score average"})
    bad = soup.findAll("div", {"class": "score bad"})

    scores = []
    for div in good:

        scores.append(div.contents[0].strip())

    for div in average:
        scores.append(div.contents[0].strip())

    for div in bad:
        scores.append(div.contents[0].strip())

    sub_companies = dict(zip(companyNames,scores))
    all_companies.update(sub_companies)

def get_all_subcategories(categoryURL):
    response = requests.get(categoryURL)

    soup = BeautifulSoup(response.text, 'html.parser')

    buttons = soup.findAll("a", {"class": "btn btn-ecra btn"})

    sub_links = []
    for guide in buttons:
        sub_links.append(guide['href'])
    for i in sub_links:
        sub_scraper('https://www.ethicalconsumer.org/' + i)
    print("ur great")

fat_categories  = ['https://www.ethicalconsumer.org/energy','https://www.ethicalconsumer.org/fashion-clothing',
'https://www.ethicalconsumer.org/fashion-clothing','https://www.ethicalconsumer.org/food-drink',
'https://www.ethicalconsumer.org/health-beauty','https://www.ethicalconsumer.org/home-garden',
'https://www.ethicalconsumer.org/money-finance','https://www.ethicalconsumer.org/retailers',
'https://www.ethicalconsumer.org/technology','https://www.ethicalconsumer.org/transport-travel']

for f in fat_categories:
    get_all_subcategories(f)

with open('result.json', 'w') as fp:
    json.dump(all_companies, fp)


print(all_companies)
