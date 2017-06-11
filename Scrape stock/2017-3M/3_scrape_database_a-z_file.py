# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 19:04:20 2016

@author: Home
"""


import urllib2

filename = open('002_stockindex_A-Z.txt','r')
prelink = 'https://www.set.or.th/set/commonslookup.do?language=en&country=TH&prefix='
count = 0

for name in filename:
    name = name.strip()
    url = prelink + name
    f = open('003_'+str(name)+'.txt','w')
    
    page = urllib2.urlopen(url)
    content = page.read()
    page.close()
    
    f.write(str(content))
    f.close()
        
    count +=1
print count

filename.close()

print 'finish "scrape a-z file"'
