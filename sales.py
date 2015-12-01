from bs4 import BeautifulSoup
import re
import requests


def jcrew(soup):
    promoText = soup.find('span', {'class': 'global-header-text'}).text
    promoDetails = soup.find('div', {'id': 'globalHeaderDisclaimertext'}).text
    return promoText,promoDetails

def nyc(soup):
    promoText = soup.select("#promotTitle")[0]['value']
    promoDetails = soup.find('input', {'id': 'promotMessage'})['value']
    return promoText, promoDetails

def vra(soup):
    saleDetails = soup.select("#promo_fade")[0]
    saleDetails = saleDetails.select('li')
    promoText = saleDetails[0].text
    promoDetails = ""
    for deal in saleDetails:
        promoDetails += deal.text + "\n"
    return promoText, promoDetails

def findSales(company, url):
    """Takes in a company and the url name
        Return the companies promo and details"""

    #Make a request to the url

    soup = ""
    try:
        response = requests.get(url, timeout=(10.0, 1.0))
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
    except requests.exceptions.ConnectTimeout as e:
        print "Request to " + company + "timed out. Please check url"
        return None, None


    if company == "jcrew":
        return jcrew(soup)
    elif company == "nyc":
        return nyc(soup)
    elif company == "vra":
        return vra(soup)
    else:
        return None, None


if __name__ == '__main__':
    print "here"
    pT, pD = findSales("vra", "http://www.verabradley.com/")
    print pD