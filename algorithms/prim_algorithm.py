import heapq
import sys

class Graph:
    def __init__(self, g):
        self.g = g

    def __repr__(self):
        return str( self.g )

    def __len__(self):
        return len(self.g)

# class Queue:
#     def __init__(self, arr):
#         # This is a minheap
#         self.arr = []

#         for item in arr:
#             self.arr.append(item)
#             self.sift_up(len(self.arr) - 1)

#     def __len__(self):
#         return len(self.arr)


#     def sift_up(self, i):
#         while (i - 1) // 2 >= 0 and self.arr[ (i-1)//2 ] > self.arr[i]:
#             self.arr[(i-1)//2], self.arr[i] = self.arr[i], self.arr[(i-1)//2]
#             i = (i-1) //2

#         return i

#     def append(self, v):
#         self.arr.append(v)
#         self.sift_up(len(self.arr) - 1)

#     def pop(self):
#         self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]

#         r = self.arr.pop()

#         self.sink_down(0)

#         return r

#     def pop_all(self):
#         while self.arr:
#             print(self.pop())


#     def sink_down(self, i):
#         smallest = i

#         while True:

#             left = 2*i + 1
#             right = 2*i + 2

#             if left < len(self.arr) and self.arr[left] < self.arr[smallest]:
#                 smallest = left

#             if right < len(self.arr) and self.arr[right] < self.arr[smallest]:
#                 smallest = right

#             if smallest == i:
#                 break

#             self.arr[smallest], self.arr[i] = self.arr[i], self.arr[smallest]

#             i = (smallest)

#     def __repr__(self):
#         return str(self.arr)

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

def prim(graph, u):
    n = len(graph)

    visited = [0 for _ in range(len(graph))]

    parent = [-1 for _ in range(n)]

    keys = [sys.maxsize for _ in range(n)]
    keys[u] = 0

    min_heap = []
    heapq.heappush(min_heap, [0, u, -1])

    while min_heap:

        _, u, _ = heapq.heappop(min_heap)

        # Everything that is popped out of the minheap is confirmed to be finalised
        visited[u] = 1

        for v in range(n):
            if visited[v] != 1 and graph.g[u][v] > 0 and keys[v] > graph.g[u][v]:
                # keys[v] > graph.g[u][v] means that are updating the parent arr if the current path to the vertex is not the minimum
                # graph.g[u][v] > 0 means if it is 0 or less it is not directly connected
                # visited[v] != 1 exclude finalised vertex (i.e. edge going in is confirmed to be the min)

                keys[v] = graph.g[u][v]
                parent[v] = u
                heapq.heappush(min_heap, [graph.g[u][v], u, v])

    return parent





if __name__ == "__main__":
    # h = Queue([3,2,3,4,1,2,4,5,6,7,1])
    # h.pop_all()
    graph1 = [
        [0, 2, 3],
        [0, 0, 1],
        [0, 0, 0]
    ]

    g = Graph(graph1)

    print(prim(g, 0))
