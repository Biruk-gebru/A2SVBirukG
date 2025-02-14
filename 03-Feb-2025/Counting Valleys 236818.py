# Problem: Counting Valleys - https://www.hackerrank.com/challenges/counting-valleys/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    count = 0
    level = 0
    flag = False
    for i in range(steps):
        if path[i] == "D":
            level -= 1
        else:
            level += 1
        print(level)
        if level < 0:
             flag = True
        if level == 0 and flag == True:
            count += 1
            flag = False
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
