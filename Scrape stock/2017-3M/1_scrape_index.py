# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 19:04:20 2016

@author: Home
"""

import urllib2

url = 'http://www.set.or.th/set/commonslookup.do?msg=nf&amp;language=th&amp;country=TH'
page = urllib2.urlopen(url)
content = page.read()
page.close()
   
f = open('001_scrape_index.txt','w')
f.write(str(content))
f.close()

print 'finish "scrape index"'
