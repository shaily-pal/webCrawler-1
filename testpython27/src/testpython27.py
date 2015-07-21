import urllib2
import re

f = open('database.txt', 'a')
#connect to a URL
web = urllib2.urlopen("http://gktoday.in/")

#read html code
html = web.read()

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

f.write(str(links))
    

