class Solution(object):
    def insert(self, intervals, newInterval):
        # :type intervals: List[List[int]]
        # :type newInterval: List[int]
        # :rtype: List[List[int]]
        # Beats 92.53%
        # Initally put break on line 13 not return res

        res = []

        for i in range(len(intervals)):
            # Handle edge cases

            if newInterval[1] < intervals[i][0]:
                #newInterval is before the current interval with no overlap
                res.append(newInterval)
                res += intervals[i:]

                # return not break!
                return res
            elif newInterval[0] > intervals[i][1]:
                #newInterval is after the curret interval in which case it is safe to store the current interval
                res.append(intervals[i])
            else:
                # newInterval overlaps with the current interval
                # Update newInterval

                # The new interval is the min of first index and max of the second index
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)

        return res

