#!/usr/bin/python

import sys
from ipdb import set_trace as st

def rock_paper_scissors(n):
  # Your code here
  if n == 1:
    return [["rock"], ["paper"], ["scissor"]]
  one_n_less = rock_paper_scissors(n-1)
  result = []
  for choice in [["rock"], ["paper"], ["scissor"]]:
    temp_lst = [choice + i for i in one_n_less]
    # st()
    result.extend(temp_lst)
  return result


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')