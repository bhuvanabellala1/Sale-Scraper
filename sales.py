from bs4 import BeautifulSoup
import re
import requests


def jcrew(htmlText):

    html = htmlText.text
    soup = BeautifulSoup(html, "html.parser")
    promoText = soup.find('span', {'class': 'global-header-text'}).text
    promoDetails = soup.find('div', {'id': 'globalHeaderDisclaimertext'}).text
    return promoText,promoDetails



def findSales(company, url):
    """Takes in a company and the url name
        Return the companies promo and details"""

    #Make a request to the url

    response = ""
    try:
        response = requests.get(url, timeout=(10.0, 1.0))
    except requests.exceptions.ConnectTimeout as e:
        print "Request to " + company + "timed out. Please check url"
        return None, None


    if company == "jcrew":
        return jcrew(response)
    else:
        return None, None


if __name__ == '__main__':
    findSales("jcrew", "https://www.jcrew.com/index.jsp")
