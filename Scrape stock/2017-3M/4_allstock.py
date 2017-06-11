# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 19:32:06 2016

@author: Home
"""
count = 0
filename = open('002_stockindex_A-Z.txt','r')
content1 = filename.read()
filename.close()
lists = content1.split('\n')

f2 = open('004_allstock.txt','w')
start = '                          <td><a href="/set/companyprofile.do?symbol='
start2 = 'target="">'
end2 = '</a></td>'
for letter in lists[:-1]:
    name = '003_'+str(letter)+'.txt'
    f = open(name,'r')
    lines = f.readlines()
    f.close()
    print name

    for line in lines:
        if line.startswith(start):
            line2 = line.split(start2)[1].split(end2)[0]
            f2.write(line2)
            f2.write('\n')
            print line2
            count +=1
        else:
            continue
    #f.close()
f2.close()
filename.close()
print '#############################'
print count
print 'finish "scrape stock name"'

#######################
# 004_allstock.txt
#######################
