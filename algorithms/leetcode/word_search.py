class Solution(object):
    def exist(self, board, word):
        # :type board: List[List[str]]
        # :type word: str
        # :rtype: bool
        # https://leetcode.com/problems/word-search/
        # Beats 40%
        # Forgot to check for next node indices are less than 0
        # Messed up m and n on visisted array
        # Forgot once a path does not lead to the word, you should unmark it (set it back to 0) in the visited matrix before returning False 
        # You can also mark visited to 0 upon returning True as well so you don't have to recreate a visited arr every time

        m = len(board)
        n = len(board[0])

        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(i, j, s, c, visited):
            # print(s + board[i][j])
            if s + board[i][j] == word:
                return True
            elif s + board[i][j] != word[:c + 1]:
                return False

            visited[i][j] = 1
            # print(visited)

            for x, y in d:
                if 0 <= i + x < m and 0 <= j + y < n and visited[i+x][j+y] == 0:
                    if dfs(i + x, j + y, s + board[i][j], c + 1, visited):
                        visited[i][j] = 0  # Backtrack for reusability
                        return True

            # once a path does not lead to the word, you should unmark it (set it back to 0) in the visited matrix before returning False
            visited[i][j] = 0  # Backtrack
            return False

        v = [ [0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, '', 0, v):
                        return True

        return False
        

a = Solution()
# print(a.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))
# print(a.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))
# print(a.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(a.exist([["a", "a"]], "aaa"))

