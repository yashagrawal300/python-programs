#Link to the question --> https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    dict={}
    #print(h[1])
    c=0
    for i in range(97,123):
        #print(h[c]," ",chr(i))
        dict[chr(i)]=h[c]
        c=c+1
    maxi=0
    for j in range(len(word)):
        res=dict[word[j]]
        if (res>maxi):
            maxi=res
    
    return maxi*len(word)
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
