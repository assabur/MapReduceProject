#!/usr/bin/env python3
import sys ,re

current_word = None
current_count = 0
word = None
current_dure = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split(';', 1)
    Longword = re.split(':|;',line)
    word = Longword[0]
    dure = Longword[2]
    # convert count (currently a string) to int
    try:
        count = int(count)
        dure = int(dure)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
        current_dure +=dure
    else:
        if current_word:
            # write result to STDOUT
            dureMoy = current_dure/current_count
            dureMoy = round(dureMoy,2)
            print('%s;%s' % (current_word, dureMoy))
        current_count = count
        current_word = word
        current_dure = dure


# do not forget to output the last word if needed!
if current_word == word:
    dureMoy = current_dure/current_count
    dureMoy = round(dureMoy,2)
    print('%s;%s' % (current_word, dureMoy))
