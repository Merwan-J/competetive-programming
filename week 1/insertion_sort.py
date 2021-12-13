#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, li):
    crnt_value = li[-1]
    crnt_index = n-1
    for j in range(n):
        compare_index = crnt_index - 1

        if crnt_value < li[compare_index]:
            li[crnt_index] = li[compare_index]
            crnt_index -= 1
            compare_index -= 1
        print(*li)
        if compare_index == -1 or crnt_value > li[compare_index]:
            li[compare_index + 1] = crnt_value
            print(*li)
            break
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
