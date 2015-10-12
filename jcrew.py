from bs4 import BeautifulSoup
import re
import requests


def findSales(url=None):

    if url != None:
        try:
            print "HERE"
            jcrewResponse = requests.get(url)
            print jcrewResponse
            html = jcrewResponse.text
            print "Here"
            soup = BeautifulSoup(html, "html.parser")
            promoDetails = soup.find('div', {'id': 'globalHeaderPromoContainer'})
            promoText = promoDetails.find('span', {'class': 'global-header-text'}).text
            details = promoDetails.find('div', {'id': 'globalHeaderDisclaimertext'}).text
            return promoText,details
        except:
            return "Error getting sale info!", None

    else:
        return None, None


if __name__ == '__main__':
    findSales("https://www.jrew.com/index.jsp")
