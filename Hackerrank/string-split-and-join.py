#Problem link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    line_list = line.split(" ")
    return "-".join(line_list)
  
  
  #input: this is a string
  #output: this-is-a-string
