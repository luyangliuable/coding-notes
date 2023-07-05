import sys

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Beats 70%
        c = [ [sys.maxsize] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # Word 1 is column
        # word 2 is row

        # Make the base cases which is basically the len of each word


        for i in range(len(word1)):
            # Every row for word 1
            c[i][len(word2)] = len(word1) - i

        for j in range(len(word2)):
            c[len(word1)][j] = len(word2) - j

        # Run the algorithm
        for i in range(len(word1) - 1, - 1, -1):
            for j in range(len(word2) - 1, -1, -1):
                # i is every row for word 1
                # j is every column for word 2

                if word1[i] == word2[j]:
                    c[i][j] = c[i+1][j+1]
                else:
                    c[i][j] = min(c[i+1][j], c[i][j+1], c[i+1][j+1])

        return c[0][0]
