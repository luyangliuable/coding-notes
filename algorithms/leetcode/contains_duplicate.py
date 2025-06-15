from typing import List 

class Solution:
    def containsNearbyDuplicate(self, nums: int, k):
        num_indices = {}

        for i, num in enumerate(nums):
            if num in num_indices and i - num_indices[num] <= k:
                return True
            num_indices[num] = i

        return False


if __name__ == '__main__':
    nums = [1,2,3,1]
    k = 3

    a = Solution()
    print(a.containsNearbyDuplicate(nums, k))

    nums = [1,0,1,1]
    k = 1

    print(a.containsNearbyDuplicate(nums, k))
