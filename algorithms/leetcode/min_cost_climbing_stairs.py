class Solution(object):
    def minCostClimbingStairs(self, cost):
        # :type cost: List[int]
        # :rtype: int
        # Beats 88.50%!!! Yay!
        # Beats 99.35% memory usage! WOW!!!!
        # NOTES:
        # Used rolling approach len(DP) = 2 to conserve more space.
        # First time made a i % 2 not i % 1 which was wrong
        # First time did len(cost) for loop which is wrong because it thinks it ends at len(cost) - 1


        DP = [-1 for _ in range(2)]

        DP[0] = cost[0]
        DP[1] = cost[1]

        a = 0

        for i in range(2, len(cost)+1):
            a = i % 2

            if i == len(cost):
                DP[a] = min(DP[a-1], DP[a-2])    
            else:
                DP[a] = min(DP[a-1], DP[a-2]) + cost[i]

        return DP[a]


a = Solution()
# print(a.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
print(a.minCostClimbingStairs([0,0,0,1]))
