# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 21:25:00 2017

@author: emma
"""


##program show song & key
##select key & display song e.g.C
##show song & artist list
##select song to see chord

#name_scrape = "scrape_artist_"+x+".txt"



#/คอร์ด/กระแซ๊ะเข้ามาซิ/
#name = raw_input('enter song name: ')
#print name

##scrape index
import urllib2

def get_songchord():
##find song name
    def scrape_phase(content,start_word,stop_word):
        start_phase = content.find(start_word)
        stop_phase = content.find(stop_word,start_phase)
        chord = content[start_phase+len(start_word):stop_phase]
        return chord  
    
    def get_all_song():
        try:
            start_word = 'href="http://chordcafe.com/คอร์ด/'
            stop_word = '/"'  
            song_name = scrape_phase(content,start_word,stop_word)
            return song_name
        except:
            return None
  
    def find_url(content):
        keyfind = '<span title="'
        keycut = '<span title='
        starturl = content.find(keyfind)
        if starturl < 0:
            return None,0
        else:
            startquote = starturl+len(keycut)
            stopquote = content.find('"',startquote+1)
            url1 = content[startquote+1:stopquote]
            return url1,stopquote
        
    def get_all_link(content):
        chords = []
        while True:
            link,endpos = find_url(content)
            if link:
                chords.append(link)
                content = content[endpos:]
            else:
                break
        
        first_chords = chords[0]
        print first_chords
        return chords,first_chords
    
    def get_artist(content):
        start_word = '<h2>by'
        stop_word = '</h2>'  
        artist_name = scrape_phase(content,start_word,stop_word)
        artist_name.strip()
        return artist_name
        
    
    song_name = get_all_song()
    chords,first_chords = get_all_link(content)
    artist_name = get_artist(content)
    
    
    return song_name,chords,first_chords,artist_name

name = 'songlist_all.txt'


path = 'E:\\py\\Chordcafe\\songlist_all.txt'
f = open(path,'r')
lists = f.readlines()
f.close()
print lists
#lists =  ['/คอร์ด/คู่แท้/']

f2 = open('list_all_chord.txt','w')
for line in lists:
    i = line.strip()
    if i.find('คอร์ด') == -1:
        print i+'>> topic not found'
    else:
        url = "http://chordcafe.com"+i
        print url

    s =  urllib2.urlopen(url)
    content = s.read()
    s.close()
    
    song_name = i[17:-1]
    print song_name
    
    f = open("scrape_chord_"+song_name+".txt",'w')
    f.write(content)
    f.close()
    
    song_name,chords,first_chords,artist_name = get_songchord()
    text = 'key'+first_chords+','+artist_name+','+song_name+'\n'
    f2.write(text)
# 2 agument save in same line , how?
# split first chord
f2.close()


    

