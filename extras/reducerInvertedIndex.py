#!/usr/bin/python
import sys
import collections

inverted_index = collections.defaultdict(list)

words=[]
for line in sys.stdin:
  data = line.split("\t")
  node_id = data[0]
  words=''.join(c for c in data[1] if c not in "'[]\"").split(',')


for word in words:
	word = ''.join(c for c in word if c not in "\\%\n{}()[]")
	word = word.lower()
	if word=="" or word==" ":
		continue
	else:
		inverted_index[word].append(node_id)

for word in inverted_index:
   print "{0}\t{1}\t{2}".format(word,inverted_index[word],len(inverted_index[word]))
