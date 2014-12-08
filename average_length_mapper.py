#!/usr/bin/env python
# encoding: utf-8
"""
Mapper program to list all the entries with node_type of question and answer.
"""
import os
import csv
import sys
def mapper():
	"""Setup reader and writer objects for Standard Input and Output with Tab delimiter"""
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
	"""Skip Header"""
	reader.next()
	for line in reader:
		if len(line) == 19: 
      		# line comes from forum_node, just pick the ones needed
      		# id, title, tagnames, author_id, body, node_type,
      		# parent_id, abs_parent_id, added_at, score, state_string,
      		# last_edited_id, last_activity_by_id, last_activity_at,
      		# active_revision_id, extra, extra_ref_id, extra_count,
      		# marked ||||| Total fields 19
	  		# parent_id exists for Answers
			post_id = line[0]
	  		body = line[4]
	  		node_type = line[5]	
      		if node_type == "question":
				# print post_id,"\t",node_type,"\t",len(body)
				writer.writerow([post_id,node_type,len(body)])
      		elif node_type == "answer":
				parent_id = line[6]
				# print parent_id,"\t",node_type,"\t",len(body)
				writer.writerow([parent_id,node_type,len(body)])
				
def main():
	mapper()

if __name__ == "__main__":
	main()
