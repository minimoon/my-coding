# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 15:13:34 2017

@author: emma
"""
## Scrape index list ##
th = "ก ข ค ง จ ฉ ช ซ ฌ ญ ฐ ฑ ฒ ณ ด ต ถ ท ธ น บ ป ผ ฝ พ ฟ ภ ม ย ร ล ว ศ ษ ส ห ฬ อ ฮ "
en = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "
## Select file ##

file_text = th
file_name = 'th'
print len(file_text)

## scrape index list ##

def add_to_list(file_text):
    start_text = 0
    lists = []
    no = 0
    while start_text < len(file_text):
        stop_text = file_text.find(" ",start_text)
        print no
        no = no+1
        print 'stop'
        print stop_text
        text = file_text[start_text:stop_text]
        text = text
        print 'len'
        print len(text)
        print 'start'
        print start_text 
        print '==========='
        start_text = stop_text+len(" ")
        lists.append(text)
    return lists

lists = add_to_list(file_text)        
print lists
    

f = open('scrape_index_'+file_name+".txt",'w')
for i in lists:
    f.write(i+'\n')
f.close()