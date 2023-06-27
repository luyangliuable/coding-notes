class Solution(object):
    def numDecodings(self, s):
        # :type s: str
        # :rtype: int

        r = 0

        if len(s) <= 0:
            return r

        # python dictionary for alphabet
        alphabet = []
        for i in range(1, 27):
            alphabet.append(chr(i + 64))

        DP = [0 for _ in range(len(s) + 1)]


        DP[0] = 1
        for i in range(2, len(s) + 1):
            c = s[i-2: i]

            if s[i-1] != '0':
                DP[i] += DP[i-1]

            if 10 <= int(c) < 27:
                DP[i] += DP[i-2]


        print(DP)
        return DP[-1]



a = Solution()
print(a.numDecodings("1234"))
print(a.numDecodings("06"))
