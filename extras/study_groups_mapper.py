#!/usr/bin/python
# encoding: utf-8

# line comes from forum_node, just pick the ones needed
# id, title, tagnames, author_id, body, node_type,
# parent_id, abs_parent_id, added_at, score, state_string,
# last_edited_id, last_activity_by_id, last_activity_at,
# active_revision_id, extra, extra_ref_id, extra_count,
# marked ||||| Total fields 19
"""
Mapper program that: 
(1) Goes through each post with node_type of "question", "answer" and "comments" 
(2) Lists all the students participated even if multiple times
"""

import os
import sys
import csv

def mapper(stdin):
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
	reader.next()
	for line in reader:
		if len(line) == 19:
			node_type = line[5]
			if node_type == "question":
				common_id = line[0] # Get the post id
				author_id = line[3]
			else:
				common_id = line[6] # Get the Parent id for "answer" and "comment"
				author_id = line[3]				
			# writer.writerow([common_id, author_id]) 
			print common_id,'\t',author_id

if __name__ == "__main__":
    mapper(sys.stdin)
