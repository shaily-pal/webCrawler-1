#!usr/bin/python
import urllib2
import re
from bs4 import BeautifulSoup
import ast


#Category 1 Current Affairs

#CODE TO FILL all_quiz_urls.txt file with all the pages which has quiz questions for current affairs
file1 = open('all_quiz_urls.txt', 'w')


current_affairs_url = 'http://www.gktoday.in/gk/current-affairs-questions-answers/'
req = urllib2.Request(current_affairs_url)
web = urllib2.urlopen(req)
page = web.read()
html_page = BeautifulSoup(page, 'html.parser')
#Make two lists
all_current_affairs_page_urls = []
quiz_urls = []

all_current_affairs_page_urls.append(current_affairs_url)
#In this case this value comes to be 19, but to process the data faster we will re-initialize the value with 3
last_page_number_tag = html_page.find("a", { "class" : "last" })
last_page_number_value = last_page_number_tag.text
last_page_number_value = 3

for i in range(2,int(last_page_number_value)+1):
    s = ''
    seq = (current_affairs_url,'page/',str(i))
    page_url = s.join( seq );
    all_current_affairs_page_urls.append( page_url)

for current_affairs_page_url in all_current_affairs_page_urls:
    req = urllib2.Request(current_affairs_page_url)
    web = urllib2.urlopen(req)
    page = web.read()
    current_affairs_page = BeautifulSoup(page, 'html.parser')
    main_div = current_affairs_page.find("div", { "class" : "posts-listing" })
    for quiz_url_div in main_div.findAll("div", { "class" : "widget widget_archive" }):
        for u in quiz_url_div.find_all('a', href=True):
            quiz_urls.append(u['href'])
file1.write(str(quiz_urls))
file1.close()


file1 = open('all_quiz_urls.txt', 'r')

#Retrieve each URL from obtained list of URLs
for quiz_url in quiz_urls:
    req = urllib2.Request(quiz_url)
    web = urllib2.urlopen(req)
    quiz_url_page = web.read()
    quiz_url_page = BeautifulSoup(quiz_url_page, 'html.parser')
   
    title = quiz_url_page.find('h1').text    
    title = ''.join(e for e in title if e.isalnum())

    file_ca = open(title+'.txt', 'w')
    
    print "Extracting questions in %s" % title
    for quiz_question in quiz_url_page.findAll("div", { "class" : "content_mirror" }):
        question_object = quiz_question.find('p').text
   
        indexA = question_object.find('[A]')
        indexB = question_object.find('[B]')
        indexC = question_object.find('[C]')
        indexD = question_object.find('[D]')
        index_not_needed = question_object.find('Show Answer')
        

        question = question_object[:indexA]
        optionA = question_object[indexA:indexB]
        optionB = question_object[indexB:indexC]
        optionC = question_object[indexC:indexD]
        optionD = question_object[indexD: index_not_needed]
        
        try:
           quiz_question.find('p',{'class':'answer'}).text
        except AttributeError:
           continue
        
        answer = quiz_question.find('p',{'class':'answer'}).text

        s = '\n'
        seq = (question.encode('ascii', 'ignore'), optionA.encode('ascii', 'ignore'), optionB.encode('ascii', 'ignore'), optionC.encode('ascii', 'ignore'), optionD.encode('ascii', 'ignore'), answer.encode('ascii', 'ignore'),'\n')
        question_to_write = s.join( seq );
        
        file_ca.write(question_to_write)
    file_ca.close()
        
        
        

