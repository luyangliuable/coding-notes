class Solution(object):
    def countSubstrings(self, s):
        # :type s: str
        # :rtype: int
        # Beats 30%
        # Finished in 8 mintues
        # Forgot to include guard case when string is empty
        # i goes up to len(s) + 1 because i represents the length of the string and it ranges up to len(s)
        # j represents the start of the string and ranges up to len(s) - i + 1 not inclusive because that is the very end plus length of substring
        # k represents the end of the string is j + i - 1, it represents the end of the string but it does not include the very end so -1

        ans = 0

        if len(s) == 0:
            return ans

        DP = [[0 for _ in range(len(s))] for _ in range(len(s))]

        ans += len(s)

        for i in range(len(s)):
            DP[i][i] = 1

        for i in range(len(s) - 1):
            if s[i+1] == s[i]:
                DP[i][i+1] = 1
                ans += 1


        for i in range(3, len(s) + 1):
            for j in range(len(s) + 1 - i):
                k = j + i - 1

                if s[k] == s[j] and DP[j + 1][k - 1] == 1:
                    DP[j][k] = 1
                    ans += 1

        return ans

a = Solution()
print(a.countSubstrings("babad"))



