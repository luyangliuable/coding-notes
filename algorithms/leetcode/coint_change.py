class SolutionTopDown(object):
    def coinChange(self, coins, amount):
        # :type coins: List[int]
        # :type amount: int
        # :rtype: int

        # Each DP slot represents minimum that makes up the amount
        # Time limit exceeded!!!

        if amount == 0:
            return 0

        DP = [amount + 1 for _ in range(amount + 1)]

        s = min(coins)

        def dfs(t):
            # Populates DP arr with min coins at each amount
            # Returns min coins at current amount t

            if t < s:
                return amount + 1

            if t == 0:
                return 0

            if DP[t] == amount + 1:
                # Only start looking for min if it is not already traverse this is key! Because it is how DP improves this
                # e.g. if 5 is already 11 -> 9 -> 5 -> 3 just need to do 11 -> 10 -> 5

                for c in coins:
                    if c <= t:
                        DP[t] = min(DP[t], 1 + dfs(t - c))

            return DP[t]

        DP[0] = 0

        for c in coins:
            if c <= amount:
                DP[c] = 1
            elif c == amount:
                return 1

        dfs(amount)

        return DP[amount] if DP[amount] != amount + 1 else -1


class Solution():
    def coinChange(self, coins, amount):
        # :type coins: List[int]
        # :type amount: int
        # :rtype: int
        # Beats 50%
        # Finished in 10 minutes
        # Forgot to loop to amount + 1 which includes amount
        # Not sure if i - c >= 0 need to check == 0
        # Not sure why top down timed out
        # Remember bottom up is better

        DP = [amount + 1 for _ in range(amount + 1)]

        DP[0] = 0

        for c in coins:
            if c < amount:
                DP[c] = 1
            elif c == amount:
                return 1

        for i in range(1, amount + 1):
            for c in coins:
                # If already visited don't it does not mean that it now has the shortest path, because starting from other coins may lead to smaller value. This is not the case for top down because it already built from the bottom by looking at all possibilities.
                if c == amount:
                    return 1

                if i - c >= 0:
                    DP[i] = min(DP[i], 1 + DP[i - c])

        return DP[amount] if DP[amount] != amount + 1 else -1

a = Solution()
print( a.coinChange([1,2,5], 11) )
# print( a.coinChange([2], 3) )
# print( a.coinChange([1], 0) )
# print( a.coinChange([2], 1) )
# print( a.coinChange([1, 2, 5], 100) )
# print(a.coinChange([186,419,83,408], 6249))
