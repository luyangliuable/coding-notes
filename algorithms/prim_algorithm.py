class Graph:
    def __init__(self, g):
        self.g = g

    def __repr__(self):
        return str( self.g )

    def __len__(self):
        return len(self.g)

class Queue:
    def __init__(self, arr):
        # This is a minheap
        self.arr = []

        for item in arr:
            self.arr.append(item)
            self.sift_up(len(self.arr) - 1)


    def sift_up(self, i):
        while (i - 1) // 2 >= 0 and self.arr[ (i-1)//2 ] > self.arr[i]:
            self.arr[(i-1)//2], self.arr[i] = self.arr[i], self.arr[(i-1)//2]
            i = (i-1) //2

        return i

    def append(self, v):
        self.arr.append(v)
        self.sift_up(len(self.arr) - 1)

    def pop(self):
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]

        r = self.arr.pop()

        self.sink_down(0)

        return r

    def pop_all(self):
        while self.arr:
            print(self.pop())


    def sink_down(self, i):
        smallest = i

        while True:

            left = 2*i + 1
            right = 2*i + 2

            if left < len(self.arr) and self.arr[left] < self.arr[smallest]:
                smallest = left

            if right < len(self.arr) and self.arr[right] < self.arr[smallest]:
                smallest = right

            if smallest == i:
                break

            self.arr[smallest], self.arr[i] = self.arr[i], self.arr[smallest]

            i = (smallest)

    def __repr__(self):
        return str(self.arr)

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

def prim(graph, u):
    visited = [0 for _ in range(len(graph))]

    T = [ [0 for _ in range(len(graph.g[0]))] for _ in range(len(graph.g))]

    min_heap = Queue([])
    min_heap.append(u)

    min_heap.


if __name__ == "__main__":
    # h = Queue([3,2,3,4,1,2,4,5,6,7,1])
    # h.pop_all()
    graph1 = [
        [0, 2, 3],
        [0, 0, 1],
        [0, 0, 0]
    ]

    g = Graph(graph1)

    prim(g, 0)
