from bs4 import BeautifulSoup
import re
import requests


def findSales(url=None):

    if url != None:
        try:
            jcrewResponse = requests.get(url)
            html = jcrewResponse.text
            soup = BeautifulSoup(html, "html.parser")
            for child in soup.find('div', {'id': 'globalHeaderPromoContainer'}).descendants:
                print child

        except:
            print "Error getting sale info!"

    else:
        print "URL given is None!"
        return


if __name__ == '__main__':
    findSales("https://www.jcrew.com/index.jsp")
