class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        # Base case
        if len(arr) == 0:
            return 0

        # Sliding window algorithm

        r = 0
        l = 0

        res = 1


        while r < len(arr) - 1:
            if r == l and arr[r + 1] != arr[r]:
                r += 1
            elif r >= 1 \
                and ( arr[r+1] > arr[r] and arr[r] < arr[r-1] ) \
                or ( arr[r+1] < arr[r] and arr[r] > arr[r-1] ):
                    r += 1
            elif arr[r+1] != arr[r]:
                # if breaks tubulence start at the last number
                l = r
                r += 1
            else:
                # Skip = sign as it does not count as part of any turbulent subarray
                r += 1
                l = r

            res = max(r - l + 1, res)


        return res


if __name__ == "__main__":
    a = Solution()
    print(a.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
    print(a.maxTurbulenceSize([4,8,12,16]))
    print(a.maxTurbulenceSize([100]))
    print(a.maxTurbulenceSize([]))
