import math
import sys
import heapq

class Solution(object):
    def minCostConnectPoints(self, points):
        # :type points: List[List[int]]
        # :rtype: int

        # Create a adjacency matrix that connects all points

        adj = [[ 0. for _ in range(len(points)) ] for _ in range(len(points))]


        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                adj[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[i][1])
                adj[j][i] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[i][1])

        m = []
        visited = [0 for _ in range(len(points))]
        key = [sys.maxsize for _ in range(len(points))]
        r = 0
        heapq.heappush(m, [0, 0])

        while m:
            u, c = heapq.heappop(m)

            visited[u] = 1

            r += c

            for v in range(len(adj[u])):
                if visited[v] != 1 and adj[u][v] > 0 and key[v] > adj[u][v]:
                    key[v] = adj[u][v]
                    heapq.heappush(m, [v, adj[u][v]])

        return r


a = Solution()

print(a.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
