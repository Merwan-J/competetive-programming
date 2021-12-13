#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(li):
    # Write your code here
    count = 0
    for i in range(len(li)):
        check = 0
        for j in range(len(li)):
            if j+1 < len(li) and li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                check +=1
                count+=1
        
        if check==0:
            # count = count + 1 if count ==0 else count
            print(f"Array is sorted in {str(count)} swaps.")
            print(f"First Element: {str(li[0])}")
            print(f"Last Element: {str(li[-1])}")
            break

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
