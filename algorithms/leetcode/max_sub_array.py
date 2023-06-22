class Solution:
    # Kadane's
    def maxSubArray(self, nums) -> int:
        current_sum = max_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum

a = Solution()

print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

print(a.maxSubArray([1]))
