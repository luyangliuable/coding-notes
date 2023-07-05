from typing import List

class Heap:
    # Implement custom heap

    def __init__(self, input: List[int]):
        self.arr = []
        for n in input:
            self.insert(n)


    def insert(self, v):
        self.arr.append(v)
        self.sift_up(len(self.arr) - 1)


    def sift_up(self, i):
        while i > 0 and self.arr[(i - 1) // 2] > self.arr[i]:
            self.arr[i], self.arr[(i-1)//2] = self.arr[(i-1)//2], self.arr[i]
            i = (i - 1)//2

        return i


    def sink_down(self, i):
        while True:

            l = i*2 + 1
            r = i*2 + 2

            s = i

            # sink down i if it is smaller than left or right
            if l < len(self.arr) and self.arr[l] < self.arr[s]:
                s = l

            if r < len(self.arr) and self.arr[r] < self.arr[s]:
                s = r

            if s == i:
                break

            self.arr[s], self.arr[i] = self.arr[i], self.arr[s]

            i = s

        return i


    def pop(self):
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]

        r = self.arr.pop()

        self.sink_down(0)

        return r


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Beats 20%
        # Took too long
        # Actual solution just use python built in tim sort reverse and get kth index -_-
        # for sifting up and not sifting up parent check i > 0 NOT (i-1)//2
        # Got confused whether to use a minheap or maxheap
        # for this kinds of questions use a minheap because minheap[0] contains the smallest of a list of the kth largest elements
        # Discard any value smaller or equal to minheap[0] which current kth largest because it is not going to contribute
        # For sink down make i = s after self.arr[i], self.arr[s] = self.arr[s] = self.arr[i]


        # Have a min heap of length k
        # If the new number is smaller than max, replace max with new value and sink it down
        # if new number is larger than max, do nothing
        # if length of heap < k, append and sift up

        h = Heap([])

        for v in nums:
            if (len(h.arr) < k):
                h.insert(v)
            elif v > h.arr[0]:
                h.arr[0] = v
                h.sink_down(0)

        return h.arr[0]
