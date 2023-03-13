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
                return True

def min_change_matrix(matrix):
    # Calculate the sums of each row, column, and diagonal
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(col) for col in zip(*matrix)]
    diag1_sum = sum(matrix[i][i] for i in range(len(matrix)))
    diag2_sum = sum(matrix[i][len(matrix) - 1 - i] for i in range(len(matrix)))

    # Determine the common value
    common_value = row_sums[0]  # Assume the common value is the sum of the first row
    if common_value not in col_sums + [diag1_sum, diag2_sum]:
        return None  # The matrix cannot be modified to have all sums equal

    # Calculate the minimum change needed to make all values equal to the common value
    min_change = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != common_value:
                # If this element is not already equal to the common value, calculate the minimum
                # change needed to make it equal
                if i == j or i == len(matrix) - 1 - j:
                    # If this is a diagonal element, the change needed is the difference between the element
                    # and the common value
                    min_change += abs(matrix[i][j] - common_value)
                else:
                    # Otherwise, the change needed is the difference between the element and the difference
                    # between the row and column sums (which are all equal to the common value)
                    min_change += abs(matrix[i][j] - (row_sums[i] - common_value))

    return min_change

if __name__ == '__main__':
    s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
    print(min_change_matrix(s))
    # formingMagicSquare(s)
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = []

    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().split())))

    # result = formingMagicSquare(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
