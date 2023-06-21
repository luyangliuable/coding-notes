class Solution(object):
    # Beats only 11% time complexity
    # Beats 90% space complexity
    # Finished in 40 minutes
    # Got a little bit confused with which heap to use (max or min)
    # Forgot to get the length of array after appending (did it before appending) leading to wrong results


    def swap(self, i_a, i_b):
        tmp = self.h[i_a]
        self.h[i_a] = self.h[i_b]
        self.h[i_b] = tmp

    def reset(self):
        self.h = []

    def sum(self, arr):
        return arr[0]**2 + arr[1]**2

    def kClosest(self, points, k):
        # :type points: List[List[int]]
        # :type k: int
        # :rtype: List[List[int]]

        # A max heap
        self.h = []

        # Add and heapify
        for p in points:

            # if len of heap < k, append and sift up
            # print(k, len( self.h ))

            s = self.sum(p)


            if len(self.h) < k:

                self.h.append(( s, p ))

                # Get length after appending !!!
                i = len(self.h) - 1
                # While parent is smaller move current up
                while i > 0 and self.h[(i-1)//2][0] < self.h[i][0]:
                    self.swap((i-1)//2, i)
                    i = (i-1)//2

            # if len of heap >= k and new value is < heap[0], sink down heap[0] = new_val
            elif len(self.h) == k and s < self.h[0][0]:
                self.h[0] = (s, p)

                i = 0

                # Sink new value down at first index if current is larger
                while True:
                    smallest = i

                    l = i*2 + 1
                    r = i*2 + 2

                    if l < len(self.h) and self.h[l][0] > self.h[smallest][0]:
                        smallest = l

                    if r < len(self.h) and self.h[r][0] > self.h[smallest][0]:
                        smallest = r

                    if smallest == i:
                        break

                    self.swap(smallest, i)

                    i = smallest

        r = [v[1] for v in self.h]                
            
        return r


a = Solution()
print(a.kClosest([[3,3],[5,-1],[-2,4]], 2))
a.reset()
print(a.kClosest([[6,10],[-3,3],[-2,5],[0,2]], 3))
