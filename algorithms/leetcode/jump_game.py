class Solution:
    # Dynamic programming

    # Get the furthest it can jump if it is greater than or equal the length of the array then true
    # If furthest is less than the current index then it can't jump to the end

    def canJump(self, nums):
        farthest = 0
        n = len(nums)
        for i in range(n):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= n - 1:
                return True
        return False
