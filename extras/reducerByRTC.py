#!/usr/bin/python

import sys

saleMax = 0
oldKey = None
oldItem = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue
    thisKey, thisItem, thisSale = data_mapped
    #print "This Sale is:", thisSale
    if oldKey and oldKey != thisKey:
        print oldKey, "\t",oldItem, "\t", saleMax
        oldKey = thisKey
        oldItem = thisItem
        saleMax = 0
    oldKey = thisKey
    oldItem = thisItem
    if float(thisSale) !=0 and float(thisSale) > saleMax:
        saleMax = float(thisSale)
        #print "SaleMax Now is:", saleMax

if oldKey and saleMax!=0:
     print oldKey, "\t",oldItem, "\t", saleMax

