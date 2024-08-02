class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 0

        while n:
            res += n % 2
            n >>= 1

        return res

class Solution2(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 0

        while n:
            n &= n - 1
            res += 1

        return res
        

if __name__ == "__main__":
    a = Solution()
    b = Solution2()
    print(a.hammingWeight(3))
