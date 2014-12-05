#!/usr/bin/python

import sys

popularFilePath = None
popularHitCount = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    thisFilePath, thisHitCount = data_mapped
    if int(thisHitCount) > int(popularHitCount):
	popularFilePath = thisFilePath
	popularHitCount = int(thisHitCount)

if popularFilePath != None:
    print popularFilePath, "\t", popularHitCount

