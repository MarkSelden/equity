import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import re

<<<<<<< HEAD

def microScraper(url):
    # literally just pull the company ethiscore and return it
    base = 'https://www.ethicalconsumer.org'
    url = base + url
    response = requests.get(url)
    print("microScraper: " + str(response))
    
=======
all_companies = {}
def sub_scraper(url):
    response = requests.get(url)

>>>>>>> 113f2fc757c2375ac4310bdc82440f227b111d66
    soup = BeautifulSoup(response.text, 'html.parser')
    mydivs = soup.findAll("div", {"class": "product-company"})
<<<<<<< HEAD
=======

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
>>>>>>> 113f2fc757c2375ac4310bdc82440f227b111d66
    
    good = soup.findAll("div", {"class": "score good"})
    average = soup.findAll("div", {"class": "score average"})
    bad = soup.findAll("div", {"class": "score bad"})
<<<<<<< HEAD
    
    scores = []
    print(str(good))
=======

    scores = []
>>>>>>> 113f2fc757c2375ac4310bdc82440f227b111d66
    for div in good:

        scores.append(div.contents[0].strip())

    for div in average:
        scores.append(div.contents[1].strip())

    for div in bad:
<<<<<<< HEAD
        scores.append(div.contents[2].strip())
    
    print(scores)
    return(scores)
    

def scraper(url):
    
    # add product guide ending to link
    base = 'https://www.ethicalconsumer.org'
    url = base + url
    response = requests.get(url)
    print("scraper: " + str(response))

    soup = BeautifulSoup(response.text, 'html.parser')

    mydivs = soup.findAll("div", {"class": "product-company"})

    # compile array of companyURLs from list of product reviews
    companyURLs = []
    companyNames = []
    for div in mydivs:
        companyURLs.append(div.contents[3]['href'])
        text = str(div.contents[3])
        if int(text.index('>')):
            text = text[text.index('>')+1:-4]
        print(text)
        companyNames.append(text)
        
    
    print(companyNames)
        
        
    avgDict = {}
    for i in range(len(companyNames)):
        name = companyNames[i]
        score = microScraper(companyURLs[i])
        tempDict = {name:score}
        avgDict.update(tempDict)
    
    
    
    return(avgDict)
    
scraper('/transport-travel/shopping-guide/rucksacks')
    
    

def metaScraper(categoryURL): 
    response = requests.get(categoryURL)
    print("metaScraper: " + str(response))

    soup = BeautifulSoup(response.text, 'html.parser')

    #print(soup)
=======
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
>>>>>>> 113f2fc757c2375ac4310bdc82440f227b111d66

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
    json.dump(all_companies, fp)


print(all_companies)
