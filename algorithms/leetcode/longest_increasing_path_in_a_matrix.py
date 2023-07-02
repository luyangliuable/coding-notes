class Solution(object):
    def longestIncreasingPath(self, matrix):
        # :type matrix: List[List[int]]
        # :rtype: int
        # Beats 69%
        # Forgot to add one `1 + dfs(r+1, c, matrix[r][c])` instead of just dfs(r+1, c, matrix[r][c])
        # Initially kept a global arr for max but it was unncessary because each dfs returns the max and we can just track the max of every dfs return value
        # IMPORTANT: We actually don't want to revist DP[r][c] because they are already finalised (i.e. they had their neighbours fully traversed)

        n_r = len(matrix)
        n_c = len(matrix[0])

        if n_r == 0 and n_c == 0:
            return 0

        DP = [ [-1 for _ in range(n_c)] for _ in range(n_r)]

        r = 0

        def dfs(r, c, prev):

            if r < 0 or r >= n_r or c < 0 or c >= n_c or matrix[r][c] <= prev:
                return 0
            elif DP[r][c] != -1:
                return DP[r][c]


            m = 1
            m = max(m, 1 + dfs(r+1, c, matrix[r][c]))
            m = max(m, 1 + dfs(r, c+1, matrix[r][c]))
            m = max(m, 1 + dfs(r-1, c, matrix[r][c]))
            m = max(m, 1 + dfs(r, c-1, matrix[r][c]))

            DP[r][c] = m

            return m

        res = 0

        for r in range(n_r):
            for c in range(n_c):
                res = max(res, dfs(r, c, -1))

        return res

a = Solution()
print(a.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
