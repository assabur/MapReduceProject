#!/usr/bin/env python3
import sys ,re
# input comes from STDIN
for line in sys.stdin:
    UserAverage = 0
    # remove leading and trailing whitespace
    line = line.strip()
    #print(current_dure)
    # parse the input we got from mapper.py
    word, count = line.split(':', 1)
    #split with multiples delimiteur
    Longword = re.split('->|:',line)
    #print(Longword)
    UserName = Longword[0]
    # convert count (currently a string) to int
    try:
        count = int(count)
        duration = int(Longword[1])
        DurationOccurence = int(Longword[2])
    except ValueError:
        continue
   
    # calculate the average and round up values
    UserAverage= round(duration / DurationOccurence, 2)
    print('%s has an average time of %s with %s calls' % (UserName, UserAverage,DurationOccurence))

