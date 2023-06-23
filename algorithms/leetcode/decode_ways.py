class Solution(object):
    def numDecodings(self, s):
        # :type s: str
        # :rtype: int
        # Beats 20%
        # Took 1 hour
        # Confused about base conditions DP[0] = 1, DP[1] = 1 if s[0] != 0, because of s='0' hard to account
        # Forgot to take into account cases like '70' and '20' or '00'
        # Forgot that the current max is DP[i-1] + DP[i-2] not DP[i-1] + 1 because we are looking at permutations
        # Added array circular for better space complexity
        # For circular reference NEVER make w = i % len(DP) then use w. Alway use i % len(DP) to substitute i
        # i % len(DP)
        # 1 - 2 not same is (1 % 3) - 2!!!

        r = 0

        if len(s) <= 0:
            return r

        DP = [0 for _ in range(len(s) + 1)]

        DP[0] = 1 

        DP[1] = 1 if s[0] != '0' else 0

        if len(s) == 1:
            return DP[1]

        i = 0

        for i in range(2, len(s) + 1):
            # If current digit is not 0.
            if s[i-1] != '0':
                DP[i] += DP[( i - 1 )]

            # If current digit and one before makes a combo
            c = s[i-2: i]
            if 10 <= int(c) < 27:
                DP[i] += DP[( i-2 )]

        return DP[i]

a = Solution()
print(a.numDecodings("226"))
print(a.numDecodings("0"))
