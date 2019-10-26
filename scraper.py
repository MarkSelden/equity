import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json

def scraper(url):
    
    base = 'https://www.ethicalconsumer.org'
    url = base + url
    response = requests.get(url)
    print(response)

    soup = BeautifulSoup(response.text, 'html.parser')

    #print(soup)

    mydivs = soup.findAll("div", {"class": "product-company"})

    companies = []
    for div in mydivs:
        companies.append(div.contents[1].contents[0])


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

    directory = dict(zip(companies,scores))
    
    return(directory)
    
    

category = 'https://www.ethicalconsumer.org/food-drink'
response = requests.get(category)
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

with open('result.json', 'w') as fp:
    json.dump(bigDict, fp)
