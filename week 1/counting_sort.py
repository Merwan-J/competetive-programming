#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
n = input()
li = input()
li = list(map(lambda x: int(x),li.split(' ')))
def countingSort(li):
    # Write your code here
    new_li = [0 * i for i in range(max(li)+1)]
    for i in set(li):
        count = li.count(i)
        new_li[i] = count
    if len(new_li) != 100:
        n = 100 - len(new_li) 
        for i in range(n):
            new_li.append(0)
    print(*new_li[:101])

countingSort(li)
