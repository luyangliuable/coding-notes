import sys


class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        initial_value = nums[0]
        glob_max = initial_value
        local_max = initial_value
        local_min = initial_value
        total = initial_value
        glob_min = initial_value

        for n in nums[1:]:
            local_max = max(n, local_max + n)
            local_min = min(n, local_min + n)

            glob_max = max(glob_max, local_max)
            glob_min = min(local_min, glob_min)

            total += n

        if glob_max < 0:
            return glob_max

        return max(glob_max, total - glob_min)


if __name__ == "__main__":
    a = Solution()
    print(a.maxSubarraySumCircular([5, -3, 5]))
