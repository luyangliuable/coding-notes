class Solution(object):
    def subsets(self, nums):
        # :type nums: List[int]
        # :rtype: List[List[int]]

        def backtrace(f = 0, c = []):
            # Append all substr to r set of length k
            if len(c) == k:
                r.append(c[:])
                return

            # Recursively look beyond
            for i in range(f, n):

                c.append(nums[i])
                backtrace(i + 1, c)
                c.pop()

        r = []
        n = len(nums)
        for k in range(n + 1):
          backtrace()

        return r

a = Solution()
print(a.subsets([1,2,3]))

