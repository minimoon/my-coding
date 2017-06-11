# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 19:04:20 2016

@author: Home
"""

import urllib2
from bs4 import BeautifulSoup

set = 'http://www.set.or.th/set/commonslookup.do?msg=nf&amp;language=th&amp;country=TH'
page = urllib2.urlopen(set)

soup = BeautifulSoup(page)

   
f = open('scrape_index.txt','w')


f.write(str(soup))

f.close()



print 'finish ja'
