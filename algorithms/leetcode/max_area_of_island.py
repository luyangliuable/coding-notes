class Solution(object):
    def maxAreaOfIsland(self, grid):
        # Problems:
        # For DFS passing x and y instead of x2 and y2 but rest is all correct
        # got confused and thought x is which column and y is which row. In fact x is which row and y is which column. M is the number of rows and n is number of columns. This is a convention in code.
        # Beats 82.88%
        
        m = len(grid) # Number of rows
        n = len(grid[0]) # Number of columns
        v = [ [0 for _ in range(n)] for _ in range(m)]

        curr_max = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and v[i][j] != 1:
                    curr_max= max(curr_max, self.dfs(grid, v, i, j))

        return curr_max

    def dfs(self, grid, v, x, y):
        # X is row index
        # Y is column index

        m = len(grid)
        n = len(grid[0])
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        v[x][y] = 1

        a = 1 # New area from further dfs

        for dx, dy in d:
            x2 = x + dx
            y2 = y + dy
            if 0 <= x2 < m and 0<= y2 < n and v[x2][y2] == 0 and grid[x2][y2] == 1:
                a += self.dfs(grid, v, x2, y2)

        return a

a = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(a.maxAreaOfIsland(grid))
