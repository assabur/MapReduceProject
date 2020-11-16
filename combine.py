#!/usr/bin/env python3
import sys
from collections import defaultdict
CurrentName = None
CurrenUsertPhoneNumber = 0
CallFrom = 0
CurrentCallDuration = 0
UserDirectory = defaultdict(list)
CallDirectory = defaultdict(list)
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    CurrentName, CurrenUsertPhoneNumber, CallFrom, CurrentCallDuration = line.split('->')
    #rangement dans le dico des users
    if CurrentName != "None":
        UserDirectory[CurrentName].append(CurrenUsertPhoneNumber)
    #rangement dans le dico des calls
    elif CallFrom != "0":
        CallDirectory[CallFrom].append(CurrentCallDuration)

UserCallDuration = defaultdict(list)
SumUserCallDuration = 0
#Visit the the user and call
#directories
for CurrentName, CurrenUsertPhoneNumber in UserDirectory.items():
    for CallFrom, CurrentCallDuration in CallDirectory.items():
        if CurrenUsertPhoneNumber[0]==CallFrom:#make test
            for i in range(len(CurrentCallDuration)):
                UserCallDuration[CurrentName].append(CurrentCallDuration[i])
                SumUserCallDuration+=int(CurrentCallDuration[i])
            print('%s->%s->%s:%s' % (CurrentName, SumUserCallDuration, len(CurrentCallDuration),1))
            #print('%s:%s:%s;%s' %(name,tel,int(Line[2].strip()), 1))
            SumUserCallDuration=0
