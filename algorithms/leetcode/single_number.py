class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0

        for n in nums:
            r ^= n

        return r

if __name__ == "__main__":
    a = Solution()
    print(a.singleNumber([1]))
