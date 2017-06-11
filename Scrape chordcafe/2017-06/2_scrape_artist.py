# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 21:25:00 2017

@author: emma
"""

#program show song & key
#select key & display song
#input song to see chord

#scrape artist
import urllib2
def add_artist(lists):
    scraped = []
    
    for i in lists:
        x = i.strip()
        print x
        url = "http://chordcafe.com/search/"+x
        print url+"\n"
#        http://chordcafe.com/search/%E0%B8%82/
        
        s =  urllib2.urlopen(url)
        content = s.read()
        s.close()
        
    
        f = open("scrape_artist_"+x+".txt",'w')
        f.write(content)
        f.close()
        scraped.append(x)
    return scraped

#find url and save in list
def find_url(content):  
    keyfind = '<a href="/chord-guitar/'
    keycut = '<a href='
    starturl = content.find(keyfind)
    print 'start'
    print starturl
    if starturl < 0:
        return None,0
    else:
        startquote = starturl+len(keycut)
        print 'startquote'
        print startquote
        stopquote = content.find('"',startquote+1)
        print 'stop'
        print stopquote
        url1 = content[startquote+1:stopquote]
        print 'url'
        return url1,stopquote
    
def get_all_link(page):
    artists = []
    while True:
        link,endpos = find_url(page)
        if link:
            artists.append(link)
            page = page[endpos:]
        else:
            break
    return artists 

file_name = 'en'

f = open('scrape_index_'+file_name+".txt",'r')
lists = f.readlines()
f.close()
print lists

print add_artist(lists)

name_artist = 'artist_name_all.txt'
f_artis_all = open(name_artist,'w')
for i in lists:
    x = i.strip()
    print x
    name_scrape = "scrape_artist_"+x+".txt"
    f = open(name_scrape,'r')
    content = f.read()
    f.close()
    
    artist_list = get_all_link(content)
    f_artis_all.write('==artist_name_'+x+'=='+'\n')
    for n in artist_list:

        f_artis_all.write(n+'\n')
    print n
f_artis_all.close()


