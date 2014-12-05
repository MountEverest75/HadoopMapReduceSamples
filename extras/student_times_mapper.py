#!/usr/bin/python
"""
Mapper program lists author_id, added_at representated as hour in 24-hour clock
"""

import csv
import sys

def mapper():
  reader = csv.reader(sys.stdin, delimiter='\t')
  reader.next()
  for line in reader:
    if len(line) == 19: 
      # line comes from forum_node, just pick the ones needed
      # id, title, tagnames, author_id, body, node_type,
      # parent_id, abs_parent_id, added_at, score, state_string,
      # last_edited_id, last_activity_by_id, last_activity_at,
      # active_revision_id, extra, extra_ref_id, extra_count,
      # marked ||||| Total fields 19
      author_id = line[3]
      added_at = line[8][11:13]	 
      print author_id,'\t',added_at 

def main():
  mapper()

if __name__ == "__main__":
  main()
