#!/usr/bin/python
import urllib2
import re
from bs4 import BeautifulSoup

file1 = open('database.txt', 'w')
file2 = open('scienceQuiz.txt', 'w')

req = urllib2.Request('http://gktoday.in/')

#connect to a URL
web = urllib2.urlopen(req)

#read html code
html = web.read()

#urlcheck = ("((http|ftp)s?://.*?)")

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

#write the extracted URL's to file1
file1.write('File containing URLS from gktoday.in\n\n\n')
for tup in links:
    for tup0 in tup:
        file1.write(str(tup0))
        file1.write("\n")
        break
    
#connect to science quiz URL
html = urllib2.urlopen('http://www.gktoday.in/objective-questions/science-technology/')
soup = BeautifulSoup(html)

file2.write('File containing single extracted URL html \n\n\n')
file2.write(str(soup))
file2.close()

#import mmap
#f = open('database.txt')
#s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
#if s.find('science') != -1:
 #   print 'true'#
  #  print s.seek(0)
    