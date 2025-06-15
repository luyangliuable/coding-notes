from typing import List 

class Solution:
    def removeDuplicates(self, nums: List[int]):
        if len(nums) <= 2:
            return len(nums)
        
        i = 0
        for num in nums:
            if i < 2 or num > nums[i - 2]: # i < 2 to ignore first 2
                nums[i] = num
                i += 1
        
        return i


if __name__ == '__main__':
    a = Solution()
    arr = [0,0,0,1,1,1,1,1,1,2,2,2,3,3]
    print(a.removeDuplicates(arr))
    print(arr)
    
