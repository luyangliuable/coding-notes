from typing import List
import sys

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Beats only 5%
        # Had a lot of issues and realised checking the base conditoins in dfs is a lot easier instead of checking first before dfs into

        c = [[sys.maxsize for _ in range(len(grid[0]))] for _ in range(len(grid))]
        v = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        d = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        def dfs(i, j, w=0):
            # Base case
            # pass any of the boundaries
            # visited
            # doesn't have an orange
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0 or v[i][j] != 0 or c[i][j] <= w:
                return

            c[i][j] = w
            v[i][j] = 1

            for dx, dy in d:
                dfs(i + dx, j + dy, w + 1)

            # for reusing visited array
            v[i][j] = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    # COntamination starts with rotten organge with a 2
                    dfs(i, j, 0)

        max_time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and c[i][j] == sys.maxsize:
                    # If there is a 1 it means there is a fresh orange
                    # if there is sys.size it means a fresh orange as well
                    return -1
                if c[i][j] != sys.maxsize:
                    max_time = max(max_time, c[i][j])

        return max_time
