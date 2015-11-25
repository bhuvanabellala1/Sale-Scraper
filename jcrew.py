from bs4 import BeautifulSoup
import re
import requests


def jcrew(htmlText):

    html = htmlText.text
    soup = BeautifulSoup(html, "html.parser")
    promoDetails = soup.find('div', {'id': 'globalHeaderPromoContainer'})
    promoText = promoDetails.find('span', {'class': 'global-header-text'}).text
    #details = promoDetails.find('div', {'id': 'globalHeaderDisclaimertext'}).text
    details = None
    return promoText,details



def findSales(company, url):

    response = ""

    try:
        response = requests.get(url, timeout=(10.0, 1.0))
    except requests.exceptions.ConnectTimeout as e:
        print "Request to " + company + "timed out. Please check url"


    if company == "jcrew":
        return jcrew(response)
    else:
        return None, None


if __name__ == '__main__':
    findSales("jcrew", "https://www.jcrew.com/index.jsp")
