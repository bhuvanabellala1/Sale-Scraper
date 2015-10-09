from bs4 import BeautifulSoup
import re
import requests


def findSales(url=None):

    if url != None:
        try:
            jcrewResponse = requests.get(url)
            html = jcrewResponse.text
            soup = BeautifulSoup(html, "html.parser")
            promoDetails = soup.find('div', {'id': 'globalHeaderPromoContainer'})
            promoText = promoDetails.find('span', {'class': 'global-header-text'}).text
            details = promoDetails.find('div', {'id': 'globalHeaderDisclaimertext'}).text
            return promoText,details
        except:
            print "Error getting sale info!"

    else:
        print "URL given is None!"
        return


if __name__ == '__main__':
    findSales("https://www.jcrew.com/index.jsp")
