# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 20:09:53 2016

@author: Home
"""


f = open('scrape_index.txt','r')

start ='<a href="/set/commonslookup.do?language=th&amp;country=TH&amp;prefix='

start2 = 'prefix='
end2 = '">'
lines = f.readlines()
count = 0
f2 = open('stockindexAZ.txt','w')

for line in lines:
    line2 = line.strip()
    if line2.startswith(start):
        line2 = (line2.split(start2))[1].split(end2)[0]
        f2.writelines(str(line2))
        f2.write('\n')
        print str(line2),
        count +=1
print count
f2.close()
        
f.close()




        


