class Solution(object):
    def searchMatrix(self, matrix, target):

        s = [matrix[i][0] for i in range(len(matrix))]

        # Binary search on first column to see which row the target is on
        a = self.specialBinarySearch(s, target)

        # Binary search on the only possible row the might contain the target.
        return True if self.normalBinarySearch(matrix[a], target) > -1 else False


    def specialBinarySearch(self, arr, target):
        # Returns the possible the target is in by getting the closest row and the row before it.

        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = lo + (hi - lo)//2

            if arr[mid] == target:
                return mid
            elif mid + 1 < len(arr) and arr[mid] < target and arr[mid + 1] > target:
                return mid
            elif mid + 1 == len(arr) and arr[mid] <= target: # condition for the last row
                return mid
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1


    def normalBinarySearch(self, arr, target):
        hi = len(arr) - 1
        lo = 0


        while lo <= hi:
            mid = lo + ( hi - lo )//2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1


a = Solution()
print(a.searchMatrix([[3,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(a.searchMatrix([[1],[3],[5]], 5))


