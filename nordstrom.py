from bs4 import BeautifulSoup
import re
import requests


def nordstrom(htmlText):

    html = htmlText.text
    soup = BeautifulSoup(html, "html.parser")
    promoDetails = soup.find('div', {'id': 'site-branding'})
    promoText = promoDetails.find('section', {'class': 'text-promo'}).text
    details = promoDetails.find('h2').text
    return promoText,details



def findSales(company, url):

    htmlText = ""

    try:
        htmlText = requests.get(url)
    except:
        return "Error getting sale info!", None

    if company == "nordstrom":
        return nordstrom(htmlText)
    else:
        return None, None


if __name__ == '__main__':
    promoText,details = findSales("nordstrom", "http://shop.nordstrom.com/")
    print promoText