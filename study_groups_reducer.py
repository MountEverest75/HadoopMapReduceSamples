#!/usr/bin/python
# encoding: utf-8
"""
Reducer program identifies the intensity of communication based on the level of participation per post
(could contain questions, answers and comments). 
This is indicated by the number of times
appears.
"""
import os
import sys
import csv

def reducer():
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
	current_post_id = None
	participant_list = []
	for line in reader:
		if len(line) != 2:
			continue
		post_id, author_id = line		
		if current_post_id and current_post_id != post_id:
			# writer.writerow([int(current_post_id), participant_list])
			print current_post_id,'\t',participant_list
			current_post_id = post_id
			participant_list = []
		current_post_id = post_id
		participant_list.append(int(author_id))
	if current_post_id != None:
		# writer.writerow([int(current_post_id), participant_list])
		print current_post_id,'\t',participant_list
			
if __name__ == "__main__":
    reducer()
