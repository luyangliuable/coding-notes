import math
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = 1
        s_2 = 1

        z_c = 0

        for n in nums:
            s *= n
            if n == 0:
                z_c += 1
                continue

            s_2 *= n

        arr = [0 for _ in range(len(nums))]

        if z_c > 1:
            return arr

        for i in range(len(arr)):
            if nums[i] == 0:
                arr[i] = s_2
            else:
                arr[i] = s // nums[i]

        return arr


if __name__ == '__main__':
    a = Solution()
    nums = [1,2,3,4]
    print(a.productExceptSelf(nums))

    nums2 = [-1,1,0,-3,3]
    print(a.productExceptSelf(nums2))
