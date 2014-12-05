#!/usr/bin/python
# encoding: utf-8

# line comes from forum_node, just pick the ones needed
# id, title, tagnames, author_id, body, node_type,
# parent_id, abs_parent_id, added_at, score, state_string,
# last_edited_id, last_activity_by_id, last_activity_at,
# active_revision_id, extra, extra_ref_id, extra_count,
# marked ||||| Total fields 19
"""
Mapper program that goes through each post with node_type "question" and lists all the tagnames used in a particular post
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
			# post_id = line[0]
			node_type = line[5]
			if node_type == "question":
				tags = line[2].split()
				for tag in tags:
					# writer.writerow([tag])
					print tag
					# writer.writerow([post_id, tag])

if __name__ == "__main__":
    mapper(sys.stdin)
