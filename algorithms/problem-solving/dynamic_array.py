#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here

    lastAnswer = 0
    output = []

    arr = [[] for _ in range(n)]

    for item in queries:
        if item[0] == 1:
            # append queries[i][2] to arr[((queries[i][1] ^ 0) % 2)]
            idx = ((item[1] ^ lastAnswer ) % n)
            arr[idx].append(item[2])
        elif item[0] == 2:
            # assign the value at index queries[i][2] of arr[((arr[i][1] ^ 0 ) % 2)] to last answer
            idx = (queries[i][1] ^ lastAnswer) % n
            lastAnswer = arr[][queries[i][2]]
            output.append(lastAnswer)

    return output

if __name__ == '__main__':
    dynamicArray(2, [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]])


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     q = int(first_multiple_input[1])

#     queries = []

#     for _ in range(q):
#         queries.append(list(map(int, input().rstrip().split())))

#     result = dynamicArray(n, queries)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
