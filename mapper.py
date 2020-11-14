#!/usr/bin/python
#!/usr/bin/env python3
import re
import sys
from FonctionDure import userDuree

regex = re.compile('[^a-zA-Z]')

# input comes from STDIN (standard input)
for line in sys.stdin:
    fichier = open("calls.txt", "r")
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    #print(words)
    # increase counters
    chaine ="Paris"
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        if chaine in word:
            # tab-delimited; the trivial word count is 1
            #print(word)
            Longname = word.split(",")
            #print(Longname)
            name= Longname[0]
            tel = Longname[2]
            for tuple in fichier:
              Line = tuple.strip()
              Line = tuple.split(",")
              for values in Line :
                  if tel in values:
                    #return int(Line[2].strip())
                    name= regex.sub('', name.lower())
                    print('%s:%s:%s;%s' %(name,tel,int(Line[2].strip()), 1))


