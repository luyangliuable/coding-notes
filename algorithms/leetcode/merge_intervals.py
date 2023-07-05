from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Beats 79.54%
        # The intervals wasn't sorted on leetcode I assumed it was sorted
        # Checking lastAdded was absolutely unncessary
        r = []

        intervals.sort()

        curr = intervals[0]

        for i in range(1, len(intervals)):
            lastAdded = False

            if curr[1] < intervals[i][0]:
                # No overlap
                r.append(curr)
                curr = intervals[i]
            else:
                # There is overlap
                curr = [min(curr[0], intervals[i][0]), max(curr[1], intervals[i][1])]

        r.append(curr)

        return r


a = Solution()
a = print(a.merge([[1,3],[2,6],[8,10],[15,18]]))
