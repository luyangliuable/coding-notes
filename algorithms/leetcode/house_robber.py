class Solution(object):
    def rob(self, nums):
        # :type nums: List[int]
        # :rtype: int

        n = len(nums)

        if n == 1:
            # Only one house to rob
            return nums[0]
        elif n == 0:
            # No house to rob
            return 0

        # Contains the maximum amount that can be robbed from current
        DP = [-1 for _ in range(n)]

        # Base cases
        DP[0] = nums[0]
        DP[1] = max(DP[0], nums[1])

        for i in range(2, n):
            # If the one next is more for up to the current house the max is DP[i-1]
            DP[i] = max(DP[i-2] + nums[i], DP[i-1])
        return DP[-1]

a = Solution()
print(a.rob([2,7,9,3,1]))
print(a.rob([1,2,3,1]))
print(a.rob([]))
print(a.rob([10000]))
print(a.rob([10000, 1]))
