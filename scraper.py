import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def scraper(url)
    url = 'https://www.ethicalconsumer.org/food-drink/shopping-guide/dairy-free-ice-cream'
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

    asdf = dict(zip(companies,scores))
    print(asdf.keys())