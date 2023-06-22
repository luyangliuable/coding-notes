class Solution(object):
    def pacificAtlantic(self, heights):
        # :type heights: List[List[int]]
        # :rtype: List[List[int]]

        # Issues Encountered:
        # Spent too long on this question
        # Forgot to check x2 and y2 is less than 0
        # For checking visited used x and y instead of x2 and y2
        # Initially tried to use ford fukerson
        # Initially thought had to find common reachable points by looping both matrix n^2*m^2 time complexity!
        # Only beats 6% T_T

        m = len(heights)
        n = len(heights[0])

        # n*m time complexity, could be improved
        r = [[[0,0] for _ in range(n)] for _ in range(m)]


        for i in range(len(heights)): # This is every left edge
            # Find reachable by pacific ocean
            v = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]

            self.dfsGrid(i, 0, m, n, heights, v, r, 0)

            # Find reachable by atlantic ocean
            v = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]

            self.dfsGrid(i, n-1, m, n, heights, v, r, 1)

        for i in range(len(heights[0])): # This is every left edge
            # Find reachable by pacific ocean
            v = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]

            self.dfsGrid(0, i, m, n, heights, v, r, 0)

            v = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]

            self.dfsGrid(m-1, i, m, n, heights, v, r, 1)

        a = []

        for i in range(m):
            for j in range(n):
                if r[i][j] == [1, 1]:
                    a.append([i, j])

        return a

    def dfsGrid(self, x, y, m, n, h, v, r, f):
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


        if f:
            r[x][y][0] = 1
        else:
            r[x][y][1] = 1

        v[x][y] = 1

        for dx, dy in d:
            x2 = x + dx
            y2 = y + dy

            if 0 <= x2 < m and 0 <= y2 < n and h[x2][y2] >= h[x][y] and v[x2][y2] != 1: # If reachable and not visited
                self.dfsGrid(x2, y2, m, n, h, v, r, f)

        

a = Solution()

print(a.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
