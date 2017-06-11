# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 19:04:20 2016

@author: Home
"""


import urllib2
from bs4 import BeautifulSoup


filename = open('stockindexAZ.txt','r')

link = 'http://www.set.or.th/set/commonslookup.do?language=th&country=TH&prefix='

count = 0

for name in filename:
    name = name.strip()
    set = link+name
    f = open(str(name)+'.txt','w')
    
    page = urllib2.urlopen(set)
    soup = BeautifulSoup(page)
    f.write(str(soup))
    
    f.close()
        
    count +=1
print count

filename.close()

print 'finish ja'
