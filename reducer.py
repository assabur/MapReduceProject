#!/usr/bin/env python3
#!/usr/bin/python
#!/bin/sh
import sys, re

#current_word = None
#current_dure = 0
#current_count = 0
#word = None
dureTotal = 0
count = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #print(line)
    # parse the input we got from mapper.py
    #word, count = line.split(';', 1)
    word = re.split(':|;',line)
    #print (word)
    #wordFromMapper = word.split(":")
    #dure courante de lappel de luser
    current_dure = int(word[2])
    nom = word[0]
    tel = word[1]
    taille = int(word[3])
    # name,tel,dure,tailletableau, 1

    if count <taille:
        dureTotal = current_dure +dureTotal
        count =count+1

    else :
        if count==taille :
            # convert count (currently a string) to int
            MoyenneParUser =dureTotal/taille
            dureTotal = 0
            count = 0
            print('%s:%s:%s' % (nom,tel,MoyenneParUser))

