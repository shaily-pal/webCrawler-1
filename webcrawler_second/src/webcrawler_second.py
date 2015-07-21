inputURL = "http://www.gktoday.in/"

resultUrl = {inputURL:False}
# key is a url we want. value is True or False. True means already crawled

# from urllib import urlopen

import urllib
from urllib.parse import urlparse
import time

import pprint

from bs4 import BeautifulSoup



def processOneUrl(url):
    """fetch URL content and update resultUrl."""
    try:                        # in case of 404 error
        html_page = urlopen(url)
        soup = BeautifulSoup(html_page)
        for link in soup.findAll('a'):
            fullurl = urlparse.urljoin(url, link.get('href'))
            if fullurl.startswith(inputURL):
                if (fullurl not in resultUrl):
                    resultUrl[fullurl] = False
        resultUrl[url] = True       # set as crawled
    except:
        resultUrl[url] = True   # set as crawled

def moreToCrawl():
    """returns True or False"""
    for url, crawled in iter(resultUrl.iteritems()):
        if not crawled:
            print ("moreToCrawl found {}").format(url)
            return url
    return False

while True:
    toCrawl = moreToCrawl()
    if not toCrawl:
        break
    processOneUrl(toCrawl)
    time.sleep(2)

pprint.pprint(resultUrl)