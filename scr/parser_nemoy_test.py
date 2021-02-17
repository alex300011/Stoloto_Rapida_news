#!/usr/bin/python
import urllib
from bs4 import BeautifulSoup

u='http://www.stoloto.ru/ruslotto/game'    # our url
mu='http://www.m.stoloto.ru/ruslotto/game' # mobile version
myurl = urllib.urlopen(u)

# NOTE: we are looking for this string:<div class="bingo_ticket ruslotto">
# NOTE: At the interactive Python prompt, you may be prompted for a username
# NOTE: and password here.
# Read from the object, storing the page's contents in 's'.
#s = myurl.read()
#s = u.read()
#soup=BeautifulSoup(s,'html.parser') #or lxml instead of html.parser
soup=BeautifulSoup(open('/home/bluser/lot/raw2.html'),'lxml')
Elems=soup.select('<div class="bingo_ticket ruslotto">')
'''pretty_string=soup.prettify()
#print(prettyfied)
mypfile=open('plot','wt')
mypfile.write(pretty_string.encode('utf-8'))
#lxml was before instead of html.parser
mypfile.close()
myfile=open('mlot','wt')
myfile.write(soup.encode('utf-8'))
myfile.close()'''
print(Elems)