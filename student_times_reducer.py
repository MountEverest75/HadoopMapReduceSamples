#!/usr/bin/python
"""
Reducer gets the input from mapper sorted by author_id and performs a control break processing on author_id for every post created by a particular user/student.
"""

import sys
import csv

def reducer():
    """Setup Input Reader and Output Writer Objects"""
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    """Track current auther_id"""
    current_author_id = None
    
    """Counts accumulated for every hour for each author_id"""	
    hourly_counts_list = [0] * 24
     
    for line in reader:
        if len(line) == 2:
            author_id = line[0]
            hour = int(line[1])
	    """Control break process. author_id different from current_author_id. Write output"""			
            if current_author_id is None or author_id != current_author_id:
                if not current_author_id is None:
                    write_reduced_output(current_author_id,  hourly_counts_list, writer)
		
		"""Initialize counts for new author_id"""                
		hourly_counts_list = [0] * 24

		"""Capture the new author_id"""                                
		current_author_id = author_id

            hourly_counts_list[hour] += 1
	else:
	    continue
    write_reduced_output(current_author_id, hourly_counts_list, writer)

def get_hours(hourly_counts_list):
    """ Return the hour(s) with highest posts. There could be more than one hour """
    max_post_hours = []
    max_hour_count = -1
    for i in range(24):
        if hourly_counts_list[i] > max_hour_count:
            max_hour_count = hourly_counts_list[i]
    for i in range(24):
        if hourly_counts_list[i] == max_hour_count:
            max_post_hours.append(i)
    return max_post_hours

def write_reduced_output(author_id,  hourly_counts_list, writer):
    """
    Write output in format.
        author_id hour
    """
    hours_with_most_posts = get_hours(hourly_counts_list)
    for each_hour in hours_with_most_posts:
        student_record = [author_id, each_hour]
        writer.writerow(student_record)

if __name__ == "__main__":
    reducer()

