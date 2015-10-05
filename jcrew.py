__author__ = 'nataliegoldberg'


import urllib
import time
from bs4 import BeautifulSoup
import re
import requests


def findSales(url=None):
    counter = 0

    if url != None:
        counter += 1
        tempSnapshot = {}
        #print

        try:
            jcrewResponse = requests.get(url)
            timeStamp = time.time()
            tempSnapshot['timeStamp'] = timeStamp
            print "Time Stamp:", timeStamp
            html = jcrewResponse.text
            #print html
            soup = BeautifulSoup(html, "html.parser")
            # get sale
            for i in soup.find_all('div', {'id': 'globalHeaderPromoContainer'}):
                print i

        except:
            print "Error getting sale info!"

    else:
        print "URL given is None!"
        return


if __name__ == '__main__':
    findSales("https://www.jcrew.com/index.jsp")
