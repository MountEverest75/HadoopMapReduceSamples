#!/usr/bin/python
# encoding: utf-8
"""
Reducer to count number of times a tag appears in the output from mapper. Whenever there is a control break(tag changes), the output needs
written.
"""
import os
import sys
import csv

def reducer():
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
	current_tag = None
	tag_count = 0
	top_ten_tags = []
	for line in reader:
		if len(line) == 1:
			if current_tag and current_tag != line:
				top_ten_tags = find_if_top_ten(current_tag,tag_count,top_ten_tags)
				# writer.writerow([current_tag, tag_count])
				current_tag = line
				tag_count = 0
			current_tag = line
			tag_count += 1
			
	if current_tag != None:
		top_ten_tags = find_if_top_ten(current_tag,tag_count,top_ten_tags)
		# writer.writerow([current_tag, tag_count])
	for tag, count in top_ten_tags:
		# writer.writerow([tag, count])
		print tag,'\t',count

def find_if_top_ten(current_tag, tag_count, top_ten_tags):
	if len(top_ten_tags) < 10 or tag_count > top_ten_tags[9][1]:
		top_ten_tags.append([current_tag, tag_count])
		top_ten_tags.sort(key=lambda tag: tag[1], reverse=True)
		top_ten_tags = top_ten_tags[:10]
	return top_ten_tags
				
if __name__ == "__main__":
    reducer()
