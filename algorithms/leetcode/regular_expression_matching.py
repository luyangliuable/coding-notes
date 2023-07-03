class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Bottom up approach
        # Beats 26%

        c = [ [False for _ in  range(len(p) + 1)]  for _ in range(len(s) + 1)]

        c[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1 , -1):
                # If i is not the end and one string matches
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                # Go backward
                if j + 1 < len(p) and p[j+1] == "*":
                    # Don't use *
                    c[i][j] = c[i][j+2]

                    if match:
                        # Use *
                        # Not sure or c[i][j]
                        c[i][j] = c[i+1][j] or c[i][j]
                elif match:
                    # Match since there is no *
                    c[i][j] = c[i+1][j+1]

        return c[0][0]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Beats 93%!!!!!!!
        # Top down approach
        c = {}

        def dfs(i, j):
            # Base cases

            if (i, j) in c:
                return c[(i, j)]

            if i >= len(s) and j >= len(p):
                # Perfect Match
                return True
            elif j>= len(p):
                # Exhausted regex not finished matching s
                return False

            # match same character and s is not exhausted
            # Because it is possible p=a*b nad s=aaa
            match = i < len(s) and ( s[i] == p[j]  or p[j] == ".") # . can match anything

            # There exists an asterick
            if j + 1 < len(p) and p[j+1] == "*":

                # Either use *, dfs(i+1, j) or no use * dfs(i, j + 2)
                # If use *, the char proceeding * must match
                c[(i, j)] = (match and dfs(i+1, j) ) or dfs(i, j+2)

                return c[(i, j)]
            # There exists no asterick so we just move +1 both p and s
            elif match:
                c[(i, j)] = dfs(i+1, j+1)
                return c[(i, j)]

            # No matches
            c[(i, j)] = False
            return False

        return dfs(0, 0)
