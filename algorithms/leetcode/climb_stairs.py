class Solution(object):
    def climbStairs(self, n):
        # :type n: int
        # :rtype: int
        # Simple dynamic programming question
        # Solution Beats 75%

        # n+1 for nth stair
        DP = [-1 for _ in range(n+1)];

        # Base conditions

        DP[0] = 1 # Ground
        DP[1] = 1 # First stair


        for i in range(2, n+1):
            DP[i] = DP[i-1] + DP[i-2]

        return DP[-1]

a = Solution()
print(a.climbStairs(3))
