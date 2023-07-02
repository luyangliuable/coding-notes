import math

class Solution:
    def myPow(self, x: float, n: int) -> float:

        return math.pow(x, n)
        r = x

        if n > 0:
            for _ in range(n - 1):
                r = r*x
        elif n < 0:
            for _ in range(-n - 1):
                r = r*x
            r = 1/r
        else:
            return 1

        return r

a = Solution()
print(a.myPow(2, 10))
print(a.myPow(2.1, 3))
print(a.myPow(2, -2))
