from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Beats 90.74%
        # Incorrectly calculated which grid, should be 3*(i//3) + j // 3
        # NOT 3*(i//3) + j % 3
        D = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    a = (0, i, board[i][j])
                    b = (1, j, board[i][j])
                    c = (2, 3*(i//3) + j // 3, board[i][j])

                    if a in D or b in D or c in D:
                        return False

                    D.add(a)
                    D.add(b)
                    D.add(c)

        return True
