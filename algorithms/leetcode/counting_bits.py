class Solution(object):
    def hamming(self, n):

        r = 0

        while n:
            n &= n - 1
            r += 1

        return r

    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        r = [0 for _ in range(n + 1)]

        while n:
            r[n] = self.hamming(n)
            n -= 1

        return r

if __name__ == "__main__":
    a = Solution()
    print(a.countBits(2))
        
