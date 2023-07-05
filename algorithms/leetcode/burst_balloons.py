from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Lots of silly mistakes
        # For popping chosen balloon to pop last should be nums[l-1]*nums[i]*nums[r+1]
        # Beats we want to pop everything else first leaving only l-1, i and r + 1
        # NOT nums[i-1]*nums[i]*nums[i+1]
        # Beats 14%

        DP = {}
        nums = [1] + nums + [1]

        def dfs(l, r):
            # Base conditions
            if l > r:
                return 0

            if (l, r) in DP:
                return DP[(l, r)]

            DP[(l, r)] = 0

            for i in range(l, r + 1):
                # Choose i to pop last between range l and r
                a = nums[l-1]*nums[i]*nums[r+1]

                # dfs left
                # Similar to binary search i-1 since i is already accounted for
                a += dfs(l, i-1)
                a += dfs(i+1, r)

                DP[(l, r)] = max(a, DP[(l, r)])

            return DP[(l, r)]

        return dfs(1, len(nums) - 2)
