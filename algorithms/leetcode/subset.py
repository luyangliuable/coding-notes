class Solution(object):
    def subsets(self, nums):
        # :type nums: List[int]
        # :rtype: List[List[int]]
        # Finished in 10 mintues
        # Beats 50%
        # Confused how to prevent duplicates from showing
        # Method to prevent duplications: sort array first and only use first new element occurrence to now combo

        def backtrack(f = 0, t = []):
            r.append(t)

            for i in range(f, len(nums)):
                if i != f and nums[i] == nums[i-1]:
                    continue;

                backtrack(i + 1, t + [nums[i]])

        r = []

        nums.sort()

        backtrack()

        return r


a = Solution()
print( a.subsets([1,2,3]) )
print( a.subsets([]) )
