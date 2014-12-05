#!/usr/bin/python

# Format each line using regex:
# capture host, user, date, request, status and size

import sys
import re

regexLog = re.compile('([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)')
hitcount=0

for line in sys.stdin:
    matchLogLine = regexLog.match(line)
    if not matchLogLine:
        continue
    host, ignore, user, date, request, status, size = matchLogLine.groups()
    print host, "\t", user, "\t", date, "\t", request, "\t", status, "\t", size

