class Solution(object):
    def add(self, v):
        # Beats 86%
        # Did it in 10 minutes

        self.h.append(v)

        i = len(self.h) - 1

        # add and heapify
        while i > 0 and self.h[(i-1)//2] < self.h[i]:
            self.h[(i-1)//2], self.h[i] = self.h[i], self.h[(i-1)//2]
            i = (i-1)//2

    def reset(self):
        self.h = []

    def pop(self):
        self.swap(0, -1)
        r = self.h.pop()

        self.sink_down(0)

        return r

    def swap(self, i_a, i_b):
        tmp = self.h[i_a]
        self.h[i_a] = self.h[i_b]
        self.h[i_b] = tmp

    def sink_down(self, i):
        while True:
            l = 2*i + 1
            r = 2*i + 2

            largest = i

            if l < len(self.h) and self.h[l] > self.h[ largest ]:
                largest = l

            if r < len(self.h) and self.h[r] > self.h[ largest ]:
                largest = r

            if largest == i:
                break

            # self.h[i], self.h[largest] = self.h[largest] = self.h[i]
            self.swap(i, largest)

            i = largest

    def lastStoneWeight(self, stones):
        # :type stones: List[int]
        # :rtype: int

        self.h = []

        for s in stones:
            self.add(s)

        # Pop two and smash

        while len(self.h) > 1:
            a = self.pop()
            b = self.pop()

            r = abs(a - b)

            if r != 0:
                self.add(r)


        if len(self.h) == 0:
            return 0

        return self.h[0]

a = Solution()

print(a.lastStoneWeight([2,7,4,1,8,1]))
a.reset()
print(a.lastStoneWeight([1]))


