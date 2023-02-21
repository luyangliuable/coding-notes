#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here

    d = 0

    h = [0 for _ in range(len( s[0] ))]

    v = [0 for _ in range(len( s ))]

    for i in range(len(s)):
        for j in range(len(s[i])):
            v[i] += s[i][j]
            h[i] += s[j][i]

        d += s[len(s)-1-i][i]

    # find max
    maxi = max(d, max(h), max(v))
    print(maxi)

    # Check hori and vert matches

    flag = True

    for i in range(len(s)):
        for j in range(0, len(s) - 1 - i):
            if v[i] == h[j]:



if __name__ == '__main__':
    s = [[5, 3, 4], [1,5,8], [6,4,2]]
    formingMagicSquare(s)
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = []

    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().split())))

    # result = formingMagicSquare(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
