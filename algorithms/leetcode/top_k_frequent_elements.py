# Attempt 1 
class Solution_old(object):
    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def topKFrequent(self, nums, k):
        # :type nums: List[int]
        # :type k: int
        # :rtype: List[int]

        # Implement a max heap

        if len(nums) == 1:
            return [ nums[0] ]

        if len (nums) == 0:
            return []

        self.heap = []

        # Keep track of each index
        self.map = {}

        for n in nums:
            if n in self.map:
                # Find n already in self.map and add one and sift up because it is now large
                if (n == 0):
                    print(self.heap)
                i = self.map[n]
                self.heap[i][0] += 1

                while i > 0 and self.heap[ (i-1)//2 ][0] < self.heap[i][0]:
                    self.swap((i-1)//2, i)
                    i = (i-1)//2

            else:
                self.heap.append([ 1, n ])
                i = len(self.heap) - 1
                self.map[n] = i
                while i > 0 and self.heap[ (i-1)//2 ][0] < self.heap[i][0]:
                    self.swap((i-1)//2, i)
                    i = (i-1)//2

        print(self.heap)
        ans = []
        # Pop the first n values from the heap
        for i in range(min( k, len(self.heap) )):
            # pop
            self.swap(0, -1)

            ans.append(self.heap.pop()[1])

            # Sink down first element
            i = 0

            while True:
                largest = i

                r = 2 * i + 1
                l = 2 * i + 2

                if r < len(self.heap) and self.heap[r][0] > self.heap[largest][0]:
                    largest = r

                if l < len(self.heap) and self.heap[l][0] > self.heap[largest][0]:
                    largest = l

                if largest == i:
                    break

                self.swap(largest, i)

        return ans

# Attempt 2
class Solution:
    def swap(self, a, b):
        self.map[self.heap[a][1]] = b
        self.map[self.heap[b][1]] = a

        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def sift_down(self, i):
        # Initially did it the hard way, had a map the keep track of the index for each element and update the map every time the heap updates.
        # For some reason the leetcode website is bugged and says nums=[2,3,4,1,4,0,4,-1,-2,-1] and k=2 is wrong when the test output is same as expected

        
        while True:
            largest = i

            r = 2*i + 2
            l = 2*i + 1

            if l < len(self.heap) and self.heap[l][0] > self.heap[largest][0]:
                largest = l

            if r < len(self.heap) and self.heap[r][0] > self.heap[largest][0]:
                largest = r

            if largest == i:
                break

            self.swap(largest, i)

            i = largest

    def topKFrequent(self, nums, k):
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums[0]]

        self.map = {}

        for n in nums:
            if n not in self.map:
                self.map[n] = 1
            else:
                self.map[n] += 1

        self.heap = [[value, key] for key, value in self.map.items()]

        for i in range( len( self.heap ) ):
            self.sift_down(i)

                
        ans = []

        for _ in range(min(len(self.heap), k)):
            self.swap(0, -1)
            ans.append(self.heap.pop()[1])

            self.sift_down(0)

        return ans


a = Solution()
# print(a.topKFrequent([1,1,1,2,2,3], 2))
# print(a.topKFrequent([1], 1))
# print(a.topKFrequent([5,3,1,1,1,3,5,73,1], 3))
# print(a.topKFrequent([-1,1,4,-4,3,5,4,-2,3,-1], 3))
print(a.topKFrequent([2,3,4,1,4,0,4,-1,-2,-1], 2))
# print(a.topKFrequent([6,0,1,4,9,7,-3,1,-4,-8,4,-7,-3,3,2,-3,9,5,-4,0], 6))
