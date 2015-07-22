#!/usr/bin/python
import urllib2
import re
from bs4 import BeautifulSoup

f = open('database.txt', 'w')
fp = open('scienceQuiz.txt', 'w')

req = urllib2.Request('http://gktoday.in/')
#connect to a URL
web = urllib2.urlopen(req)

#read html code
html = web.read()
soup= BeautifulSoup(html)
#urlcheck = ("((http|ftp)s?://.*?)")

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

f.write('File containing URLS \n\n\n')
f.write(str(links))

fp.write('File containing html link \n\n\n')
fp.write(str(soup))
f.close()

#import mmap
#f = open('database.txt')
#s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
#if s.find('science') != -1:
 #   print 'true'#
  #  print s.seek(0)
    