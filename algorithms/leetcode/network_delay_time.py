import heapq
import sys
from typing import DefaultDict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Beats 80% 
        # Forgot to make the first index of heap element causing heap to sort the node index not the actual weight
        # This questions is very similar to rotten oranges where you find the max time for all nodes
        # Either runs dfs and save the min time to get to every node or use bfs

        # Construct adjacency matrix
        # adj = [ [0 for _ in range(n)] for _ in range(n)]

        # Smart! Adjacency list with dict
        # This is useful because nodes start a 1 not zero. It makes it easier to remember
        adj = DefaultDict(list)


        for u, v, w in times:
            adj[u].append([v, w])

        # Construct visited matrix
        visited = set()

        q = [(0, k)]

        r = 0

        while q:
            w1, u = heapq.heappop(q)

            if u in visited:
                continue

            visited.add(u)

            # Genius!
            # This is because the heapq will pop the max distance last
            r = w1

            for v, w2 in adj[u]:
                if v not in visited:
                    heapq.heappush(q, (w1 + w2, v))

        # Smart! If the len of visited is n this means all nodes are accounted for
        return r if len(visited) == n else -1
