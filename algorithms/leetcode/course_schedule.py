from typing import List

class Union:
    def __init__(self, n):
        self.rank = [0 for _ in range(n)]
        self.parent = [i for i in range(n)]

    def find(self, i):
        # Find the parent of a

        if i == self.parent[i]:
            return i

        # Path compression
        self.parent[i] = self.find(self.parent[i])

        return self.parent[i]

    def union(self, a, b):
        # Union by rank

        p_a = self.find(a)
        p_b = self.find(b)

        if p_a == p_b:
            # Already unioned
            return True

        if self.rank[p_a] < self.rank[p_b]:
            # rank of b is greater than a so make parent of a b
            self.parent[p_a] = self.parent[p_b]
        else:
            # rank of p_a is greater or equalto p_ba
            self.parent[p_b] = self.parent[p_a]

            if self.rank[p_a] == self.rank[p_b]:
                self.rank[p_a] += 1

        return False




class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # BEats 86%
        # Initally tried to use union find and realised it is for undirected and mst
        # Visited arr had an issue
        # Choosing data structure is extremely important! Adjancent list for can Finish makes it more efficient

        # adjacency list
        adj = [[] for _ in range(numCourses)]

        visited = [0 for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)

        def dfs(u, visited):
            if visited[u]:
                return False

            if adj[u] == []:
                # course has no prereq
                return True

            visited[u] = True

            for v in adj[u]:
                if not dfs(v, visited):
                    return False

            # reset visited for reusability
            visited[u] = 0

            # Path compression for optimisation so next time we know when to stop early
            adj[u] = []

            return True

        for s in range(numCourses):
            if not dfs(s, visited):
                return False


        return True







a = Solution()
print(a.canFinish(2, [[1,0]]))
print(a.canFinish(2, [[1,0], [0, 1]]))
