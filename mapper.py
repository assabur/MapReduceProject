#!/usr/bin/env python3
import sys,re
regex = re.compile('[^a-zA-Z]')
TownName = "Paris"
# input comes from STDIN (standard input)
for line in sys.stdin:
  UserName = None
  UserPhoneNumber = 0
  CallFrom = 0
  CallDuration = 0
  # remove leading and trailing whitespace
  line = line.strip()
  # split the line into words
  words = line.split(',')
  #it is about user.txt file
  if len(words)==5:
    if words[4] == TownName :
      UserName = words[0]
      UserPhoneNumber = words[2]
  else:
    #it is about call.txt file
    CallFrom = words[0]
    CallDuration = words[2]
  #send theses infos to combine file
  print('%s->%s->%s->%s' % (UserName, UserPhoneNumber, CallFrom, CallDuration))

