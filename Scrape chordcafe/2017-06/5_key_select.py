# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 23:39:15 2017

@author: emma
"""

import webbrowser
chord_key = raw_input('Enter key: ')
chord_key = chord_key.upper()
chord_key = 'key'+chord_key+','
print chord_key

path = 'E:\\py\\Chordcafe\\list_all_chord.txt'

f = open(path,'r')
lists = f.readlines()
f.close()
    
def find_song(lists,chord_key):
    key1 = ','
    for l in lists:
        line = l.strip()
        startline = line.find(chord_key)
        
        if startline == -1:
            None

        else:
            print line
            startquote = startline+len(chord_key)
            stopquote = line.find(key1,startquote+1)
            artist_name = line[startquote+1:stopquote]
            print artist_name
            startquote = stopquote
            song_name = line[startquote+1:]
            print 'song name=========='
            print song_name
            return artist_name,song_name
        
artist_name,song_name = find_song(lists,chord_key)

chord = '/คอร์ด/'

url = 'http://chordcafe.com'+chord.decode('utf-8')+song_name.decode('utf-8')
print url

if song_name == None:
    print "no chord"
else:
    webbrowser.open(url)


