#!/usr/bin/python
#!/usr/bin/env python3
import re
import sys
from FonctionDure import userDuree

regex = re.compile('[^a-zA-Z]')
annuaire = {}
# input comes from STDIN (standard input)
for line in sys.stdin:
    #fichier = open("calls.txt", "r")
    #preciser le fichier en entre mais pas le parcourir dans la fonction MAP
    # une ligne de lentre
    line = line.strip()
    # split the line into words
    #words = line.split(",")
    words = line.split(",")
    #print(words)
    # increase counters
    chaine ="Paris"

    #recuperons dabbord les num de telephone des personnes de paris
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #print(word)
        if len(words) == 5 and chaine in word: #je verifie bien qu'il sagit des users
            # tab-delimited; the trivial word count is 1
            #print(word)
            #Longname = word.split(",")
            #print(Longname)
            name= words[0]
            tel = words[2]
            #recuperations des users de paris sous forme cle valeur
            #la valeur etant un tableau contenant le nom de luser pour linstant
            annuaire[tel] = [name]
            #print(annuaire)
    print(annuaire)
    #recuperons dabbord les num de telephone des personnes de paris
    #print(words)
    """for word in (words):
        #print(words)
        if len(words) == 5 :
            for tuple in words:
              Line = tuple.strip()
              Line = tuple.split(",")"""
              #precisser les user DE
              #for values in Line :
                  #if tel == Line:
                    #return int(Line[2].strip())
                    #zname= regex.sub('', name.lower())
                    #print('%s:%s:%s;%s' %(name,tel,int(Line[2].strip()), 1))


