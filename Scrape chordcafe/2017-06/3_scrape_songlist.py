# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 21:25:00 2017

@author: emma
"""

#program show song & key
#select key & display song
#input song to see chord


#find url and save in list
def find_url(content):
    keyfind = '<h4><a href="/คอร์ด'
    keycut = '<h4><a href='
    starturl = content.find(keyfind)
    if starturl < 0:
        return None,0
    else:
        startquote = starturl+len(keycut)
        stopquote = content.find('"',startquote+1)
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



f = open('artist_name_all.txt','r')
lists = f.readlines()
f.close()
print lists

#limit 5 artists
lists = lists[0:2]
print lists

#scrape index
import urllib2

for line in lists:
    i = line.strip()
    if i.find('/chord-guitar/') == -1:
        print i+'>>> chord not found'
    else:
        print i+'\n'
        start_name = i.find("/",3)
        ar = i[start_name+1:-1]
        print ar+'\n'
    
        url = "http://chordcafe.com"+i
        print url+'\n'
        
        s =  urllib2.urlopen(url)
        content = s.read()
        s.close()
        
        f = open('scrape_songlist_'+ar+'.txt','w')
        f.write(content)
        f.close()

#fsong = open('scrape_songlist_bruno-mar','r')
#content = fsong.read()
#fsong.close()
  

f_song_all = open('songlist_all.txt','w')
for line in lists:
    i = line.strip()
    if i.find('/chord-guitar/') == -1:
        print i+'>> song name not found'

    else:
        start_name = i.find("/",3)
        sn = i[start_name+1:-1]
        print sn+'\n'
            
        f = open('scrape_songlist_'+sn+'.txt','r')
        content = f.read()
        f.close()
    
        song_list = get_all_link(content)
        f_song_all.write('==artist=='+sn+'\n')
        for s in song_list:            
            f_song_all.write(s+'\n')
f_song_all.close()
    

    

