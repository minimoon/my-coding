# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 22:00:49 2016

@author: Home
"""




count = 0
### import scrape
import urllib2
from bs4 import BeautifulSoup

### import date time
from datetime import datetime

#==============================================

### function: time stamp
def time_stamp():
    tstamp = datetime.now()
    return tstamp

tstart = time_stamp()

## Select stock
##1.1 Use all stock
filename = []
stockname = open('allstock.txt','r')
for name in stockname:
    name = name.strip()
    print name
    filename.append(name)
print filename
stockname.close()

print '============ choose language ================'
lg = 'en'
print lg

###1.2 Use one stock
#filename = ['au','col']
###2. Scrape data from factsheet 

linkp = 'http://www.set.or.th/set/factsheet.do?ssoPageId=3&language='+lg+'&country=TH&symbol='

for name in filename:
    name = name.upper()
    name = name.strip()
    print name
    set1 = linkp+name
    print "=================================="
    print 'URL link: '+set1
    
    page1 = urllib2.urlopen(set1)
    soup1 = BeautifulSoup(page1)
    
    f3 = open('Factsheet_'+lg+'_'+str(name)+'.txt','w')
    f3.write(str(soup1))
    f3.close()    
    count +=1

    print '>>> finish >>> scrape data: '+name
    
### recode start and end time (part2) ###

tend = time_stamp()
print '===========Time stamp==================='
print str(tstart) + ' << start'
print str(tend) + ' << end'
running_time = tend-tstart
print str(running_time) + ' << running'
print '========================================'
print count