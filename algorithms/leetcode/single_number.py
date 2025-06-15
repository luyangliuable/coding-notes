from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res = (res & ~num) | (~res & num)

        return res

    def xor(self, res, num1, num2) -> int:
        b = (res & ~num1) | (~res & num2)
        b = (b & ~num1) | (~b & num2)

        return b

if __name__ == '__main__':
    a = Solution()
    print(a.xor(0, 7, 8))

