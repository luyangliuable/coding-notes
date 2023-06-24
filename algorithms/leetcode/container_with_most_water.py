class Solution(object):
    def maxArea(self, height):
        # :type height: List[int]
        # :rtype: int
        # Beats 43.8%
        # Learnt two pointer algorithm which seems very simple
        # Thought left_i is the height of left not the index. Next time put `_i` to remember

        if len(height) < 2:
            return 0

        r = 0

        left_i = 0
        right_i = len(height) - 1

        while left_i != right_i:
            m = min(height[ left_i ], height[ right_i ])

            r = max(r, m*(right_i-left_i))

            if height[ left_i ] < height[ right_i ]:
                left_i += 1
            else:
                # If height of left and right same, doesn't matter which one because if encounter new longer one it would be same
                right_i -= 1

        return r

a = Solution()
# print(a.maxArea([1,8,6,2,5,4,8,3,7]))
print(a.maxArea([2,3,4,5,18,17,6]))

