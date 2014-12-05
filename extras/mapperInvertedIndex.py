#!/usr/bin/python
import sys
import csv
import re

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)
delimiters =('.','$',';','!','?',':','(',')','[',']','<','>','#','=','-','/',' ')
regexPattern = '|'.join(map(re.escape, delimiters))

for line in reader:
	node_id =line[0]
	data = re.split(regexPattern,line[4])
	print node_id,"\t",data


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        id = line[0]
        body = line[4]
        words = body.split()
        for word in words:
            if 'fantastic' in word.lower():
                if 'fantastically' not in word.lower():
                    print "%s\t%s\t%s" % (id, word, 1)
