class KthLargest(object):
    def __init__(self, k, nums):
        # :type k: int
        # :type nums: List[int]
        # This actually a min arr
        # Beats 40%
        # Issues:
        # After swapping elements in the heap, the variable p had been calculated before the swap occurred and i was still pointing to the old index of the smaller element.
        # Checked that r and l are less than len(self.arr) - 1 not len(self.arr)
        # sink_down method is checking if the indices of the children are less than the parent index (s), but it should be comparing the values at these indices.
        # Not checking if the child indices (r or l) are within the bounds of the array. If they're not, then you'll get an out-of-bounds error


        self.arr = []
        self.k = k

        for a in nums:
            self.add(a)
        

    def __repr__(self):
        return str(self.arr)


    def swap(self, a, b):
        self.arr[a], self.arr[b] = self.arr[b], self.arr[a]


    def sink_down(self, i):
        # Swap i with smallest and keep going down

        while True:
            r = self.right(i)
            l = self.left(i)

            s = i

            if l < len(self.arr) and self.arr[l] < self.arr[s]:
                s = l

            if r < len(self.arr) and self.arr[r] < self.arr[s]:
                s = r

            if s == i:
                break

            self.swap(s, i)
            i = s


    def sink_up(self, i):
        while i > 0 and self.arr[i] < self.arr[(i - 1) // 2]:
            self.arr[i], self.arr[(i-1) // 2] = self.arr[(i-1) // 2], self.arr[i]
            i = (i-1) // 2

    def add(self, val):
        # :type val: int
        # :rtype: int

        if len(self.arr) < self.k:
            self.arr.append(val)
            self.sink_up(len(self.arr) - 1)
        elif val > self.arr[0]:
            self.arr[0] = val
            self.sink_down(0)

        return self.arr[0]


    def right(self, i):
        return 2*i + 2


    def left(self, i):
        return 2*i + 1
             

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
a = KthLargest(3, [4, 5, 8, 2])
print(a.add(3))
print(a.add(5))
print(a.add(10))
print(a.add(9))
print(a.add(4))
print(a)
print(a.parent(len(a.arr)))
