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
