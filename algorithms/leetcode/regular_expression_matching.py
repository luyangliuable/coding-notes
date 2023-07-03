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


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Bottom up attempt 2

        c = [ [0 for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]

        # Both the string s and the pattern p are empty. When both s and p are empty, it's considered a perfect match because an empty pattern can match an empty string.

        c[len(s)][len(p)] = 1

        for i in range(len(s), -1, -1):
            # for s we consider len(s) because we want to check if s is exhausted but p stil isn't
            for j in range(len(p) -1, -1, -1):
                # for p we DO NOT consider len(p) because we don't want to consider case where p is exhausted and i either is or isn't that is what c[len(s)][len(p)] = True captures

                # s is not exhausted before p
                m = i < len(s) and ( s[i] == p[j] or p[j] == ".")

                # if next char of p is * need to reconsider
                if j + 1 < len(p) and p[j+1] == "*":
                    # Don't use the current asterick
                    c[i][j] = c[i][j + 2]

                    # Use the current asterick
                    if m:
                        # Put `or c[i][j]` as well in case c[i][j] is True
                        c[i][j] = ( c[i+1][j] or c[i][j])
                elif m:
                    # Since no * just move both strings up
                    c[i][j] = c[i+1][j+1]


        return True if c[0][0] else False

###############################################################################
#     When to know to work backwards in bottom up approach  nthe DP array?    #
###############################################################################

# Dependency Direction: If the solution to a subproblem depends on the solutions to future subproblems (e.g., position i depends on i+1, i+2, etc.), then you might want to solve the problem backwards.

# In this case the current cache c[i][j] needs the results of dfs(i+1, j), dfs(i+1, j+1) or dfs(i, j+2)

# Final State Known: In some problems, the final state of the DP is known or easier to calculate. In such cases, it's convenient to start from the end state and work backwards to the beginning.
# For example working on a maze problem and find cells that can lead to a certain location

# Base Case Direction: If your base case or cases are more naturally defined at the end of the sequence rather than at the start, it may be easier to work backwards.
# For example, in this `regular_expression_matching.py` problem the base case when i > len(s) and j > len(p) which is that target
