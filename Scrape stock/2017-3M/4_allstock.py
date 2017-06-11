# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 19:32:06 2016

@author: Home
"""
count = 0
filename = open('stockindexAZ.txt','r')
f2 = open('allstock.txt','w')
for name in filename:
    name = name.strip()
    f = open(str(name)+'.txt','r')
    lines = f.readlines()
    start = '<td><a href="/set/companyprofile.do?symbol='
    start2 = 'target="">'
    end2 = '</a></td>'
    

    
    for line in lines:
            if line.startswith(start):
                line = (line.split(start2))[1].split(end2)[0]
                f2.writelines(line)
                f2.writelines('\n')
                print line,
                count +=1

    f.close()
print count
f2.close()
filename.close()

print 'finish laew'
