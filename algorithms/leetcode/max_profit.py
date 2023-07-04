import sys
from typing import List

class OldSolution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] < prices[i]:
                    continue

                r = max(r, prices[j] - prices[i])

        return r


class SlidingWindowSolution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding window algorithm

        r = 0

        for w in range(2, len(prices) + 1):
            # w is window size

            l = 0
            r = w - 1

            while r < len(prices):
                r = max(prices[r] - prices[l], r)
                l += 1
                r += 1

        return r

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic programming
        # Store min price and max profit
        # Beats 50%

        min_price = sys.maxsize

        r = 0

        for i, p in enumerate(prices):
            min_price = min(p, min_price)

            if p > min_price:
                r = max(r, p - min_price)

        return r


a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))
print(a.maxProfit([7,6,4,3,1]))
                
