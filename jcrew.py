from bs4 import BeautifulSoup
import re
import requests


def jcrew(htmlText):

    html = htmlText.text
    soup = BeautifulSoup(html, "html.parser")
    promoDetails = soup.find('div', {'id': 'globalHeaderPromoContainer'})
    promoText = promoDetails.find('span', {'class': 'global-header-text'}).text
    details = promoDetails.find('div', {'id': 'globalHeaderDisclaimertext'}).text
    return promoText,details



def findSales(company, url):

    htmlText = ""

    try:
        htmlText = requests.get(url)
    except:
        return "Error getting sale info!", None

    if company == "jcrew":
        return jcrew(htmlText)
    else:
        return None, None


if __name__ == '__main__':
    promoText,details = findSales("jcrew", "https://www.jrew.com/index.jsp")
    print promoText