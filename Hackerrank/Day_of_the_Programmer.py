# Link to question - https://www.hackerrank.com/challenges/day-of-the-programmer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if(year==1918):
        return "26.09.%s" %(year)
    else:
        if(year<1917):
            if(year%4==0):
                return "12.09.%s" %(year)
            else:
                return "13.09.%s" %(year)
        else:
            if(year%400==0 or (year%4==0 and year%100!=0)):
                return "12.09.%s" %(year)
            else:
                return "13.09.%s" %(year)
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
