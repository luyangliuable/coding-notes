#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findNumber' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#

def findNumber(arr, k):
    # Write your code here
    for i in range(len(arr)):
        if arr[i] == k:
            print("YES")
            return 'YES'
    print("NO")
    return 'NO' 



if __name__ == '__main__':
    print(findNumber([1,2,3,4,5], 1))


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(input().strip())

#     arr = []

#     for _ in range(arr_count):
#         arr_item = int(input().strip())
#         arr.append(arr_item)

#     k = int(input().strip())

#     result = findNumber(arr, k)

#     fptr.write(result + '\n')

#     fptr.close()
