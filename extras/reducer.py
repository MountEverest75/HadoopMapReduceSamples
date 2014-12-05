#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

def reducer():
  post = [] # store current post data
  user = [] # store current user data
  currentUser = None # current user we are dealing with

  for line in sys.stdin:
    data = line.strip().split("\t")

    # data[0] will always be userId no matter what line we are at
    if currentUser and currentUser != data[0]:
      currentUser = data[0];
      if len(user) != 6 or len(post) != 10:
        continue # something weird happen with the input here, let's skip this line

      joinAndPrint(user, post)

    currentUser = data[0]
    # fields come sorrounded by " ", so take that into account
    if data[1] == "\"A\"":
      user = list(data)
    if data[1] == "\"B\"":
      post = list(data)

  if currentUser != None:
    if len(user) == 6 and len(post) == 10:
      joinAndPrint(user, post)

# Joins the information from the two lists and prints it to the output
def joinAndPrint(user, post):
    # input = [userId, "A", reputation, gold, silver, bronze]
    del user[0] # remove user id
    del user[0] # remove "A"
    # result --> [reputation, gold, silver, bronze]

    # input = [userId, "B", id, title, tagNames, nodeType, parentId, absParentId, addedAt, score]
    post.insert(5, post[0])
    post[0] = post[2] # move id to the front
    del post[1] # remove "B"
    del post[1] # remove duplicated id
    # result = [id, title, tagNames, userId, nodeType, parentId, absParentId, addedAt, score]

    # print everything tab separated
    print "\t".join(post) + "\t" + "\t".join(user)

def main():
  reducer()

if __name__ == "__main__":
  main()
