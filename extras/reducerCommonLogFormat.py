#!/usr/bin/python

import sys

oldFilePath = None
hitCount = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 6:
        # Something has gone wrong. Skip this line.
        continue
    thisHost, thisUser, thisDate, thisFilePath, thisStatus, thisSize = data_mapped
    if oldFilePath and oldFilePath != thisFilePath:
	print oldFilePath, "\t", hitCount
	oldFilePath = thisFilePath
	hitCount = 0
    oldFilePath = thisFilePath
    hitCount += 1

if oldFilePath != None:
    print oldFilePath, "\t", hitCount

