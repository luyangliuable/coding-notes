class Solution(object):
    def numDecodings(self, s):
        # :type s: str
        # :rtype: int
        # Beats 20%
        # Took 1 hour
        # Confused about base conditions DP[0] = 1, DP[1] = 1 if s[0] != 0, because of s='0' hard to account
        # Forgot to take into account cases like '70' and '20' or '00'
        # Forgot that the current max is DP[i-1] + DP[i-2] not DP[i-1] + 1 because we are looking at permutations

        r = 0

        if len(s) <= 0:
            return r

        # python dictionary for alphabet
        alphabet = []
        for i in range(1, 27):
            alphabet.append(chr(i + 64))

        DP = [0 for _ in range(len(s) + 1)]

        DP[0] = 1 

        DP[1] = 1 if s[0] != '0' else 0

        for i in range(2, len(s) + 1):
            # If current digit is not 0.
            if s[i-1] != '0':
                DP[i] += DP[i - 1]

            # If current digit and one before makes a combo
            c = s[i-2: i]
            if 10 <= int(c) < 27:
                DP[i] += DP[i-2]

        print(DP)

        return DP[-1]

a = Solution()
# print(a.numDecodings("226"))
print(a.numDecodings("0"))
