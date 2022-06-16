class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        pos = {"I": 1, "V": 2, "X": 3, "L": 4, "C": 5, "D": 6, "M": 7}

        sum = 0

        x = len(s) - 1

        while x >= 0:
            z = lookup[s[x]]

            if x > 0:
                posn = pos[s[x]]
                posm1 = pos[s[x-1]]

                a = lookup[s[x-1]]

                if posm1 <= posn + 2 and posn > posm1 :
                    sum += z
                    sum -= a
                    x -= 2
                else:
                    sum += z + a
                    x -= 2
            else:
                sum += z
                x -= 1
        return sum



if __name__ == "__main__":
    S = Solution()
    s = "MCMXCIV"
    s = "LVIII"
    s = "III"
    s = "VI"
    s = "MCDLXXVI"
    r = S.romanToInt(s)
    print(r)
