#!/usr/bin/env python
# encoding: utf-8
"""Reducer program to list all the entries with node_type of question and answer."""
import os
import csv
import sys
def reducer():
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
	answer_count = 0
	answer_total_length = 0
	question_body_length = 0
	current_id = None
	for line in reader:
		if len(line) == 3:
			post_id = line[0]
			"""Control break logic. (1) Write Answer Length Average and Question Length. (2) Reset all counts and totals"""
			if current_id is None or post_id != current_id:
				if not current_id is None:
					if answer_count == 0:
						average_answer_length = 0
					else:
						average_answer_length = float(answer_total_length)/float(answer_count)						
					writer.writerow([current_id, question_body_length, average_answer_length])	
				answer_count = 0
				answer_total_length = 0
				question_body_length = 0
				current_id = post_id
				
			node_type = line[1]
			body_length = float(line[2])
			if node_type == "question":
				question_body_length = body_length
			else:
				answer_count += 1
				answer_total_length += body_length
				
	if answer_count == 0:
		writer.writerow([current_id, question_body_length, "0"])
	else:
		writer.writerow([current_id, question_body_length,float(answer_total_length)/float(answer_count)])
	
def main():
	reducer()

if __name__ == "__main__":
	main()

