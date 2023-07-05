class TimeMap(object):
    # Beats 75.51%
    # Initially forgot Returns None instead of ""
    # Initially forgot can return any before before timestamp no exact timestamp exists
    # Does not need to sort map value each time because time always increases
    # m = (l + r) // 2 for binary search not (l + r + 1) // 2
    # while l <= r not while l < r


    def __init__(self):
        self.map = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """

        if key not in self.map:
            self.map[key] = []

        self.map[key].append([timestamp, value])


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """

        arr = []
        if key in self.map:
            arr = self.map[key]

        # Binary search
        # Get the closest value to the timestamp and before the timestamp
        l = 0
        r = len(arr) - 1

        res = ""

        while l <= r:
            m = (l + r)//2

            if arr[m][0] <= timestamp:
                res = arr[m][1]
                l = m + 1
            else:
                r = m - 1

        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


# Heap
# r = 2*i + 2
# p = ( r - 2 ) / 2 for [2, 4, 6] if i starts at 0
# p = (l - 1) / 2 for [1, 3, 5] if i starts at 0

# If p starts at 1 then p = (i) // 2
# if p starts at 0 then p = (i - 1) //22
