class OldSolution(object):
    def findRedundantConnection(self, edges):
        # :type edges: List[List[int]]
        # :rtype: List[int]

        # Node start with 1 not 0. So 0th index is 1

        n = len(edges)

        al = [[] for _ in range(n)]

        for u, visited in edges:
            al[u - 1].append(visited)

        # Perform bfs and append visited edges

        visited = [0 for _ in range(n)]

        s = []

        r = []

        for i in range( n ):
            # For every edge to prevent disconnected graphs

            s.append([-1, i])

            while len(s) > 0:
                u = s.pop()

                # If not visited start
                # if visited[u[1]] == 0:
                    # Mark start as visited
                if u[0] > -1 and visited[u[1]]:
                    r.append([u[0]+1, u[1] + 1])

                visited[u[1]] = 1

                # store all end
                for v in al[u[1]]:
                    v -= 1
                    s.append([u[1],v])


        # return r
        r.sort(reverse=True)
        print(r)
        return r[-1]
    

class Solution(object):
    def findRedundantConnection(self, edges):
        # Beats 80% time complexity and 91.7%
        # Finished in an hour
        # With union by rank and path compression algorithm
        # a sequence of m operations will cost O (m α(n )), where α(n) is the inverse Ackermann function, an extremely slowly growing function.
        # Initialialy got confused and tried breadth first search
        # We are only returing edges inside edgelist
        # Initially got the union by rank algorithm wrong, try to remember

        p = [i for i in range(len(edges))]

        r = [1] * (len(edges))

        def find(x):
            r = p[x]

            while p[r] != r:
                p[r] = p[p[r]] # Path compression

                r = p[r]

            return r

        def union(x, y):
            # Union by rank

            # Minus one because the nodes start at 1
            x -= 1
            y -= 1

            p1, p2 = find(x), find(y)

            if p1 == p2:
                # If parent are the same it means it is already unioned, the edge is redundant
                return False

            if r[p1] < r[p2]:
                # The answer in the unit handbook for uni is wrong
                # You add the rank of the parent to the new rank of current that got new stuff unioned to it
                p[p1] = p2
                r[p2] += r[p1]
            else:
                p[p2] = p1
                r[p1] += r[p2]

            return True

        for x, y in edges:
            if not union(x, y):
                return [x, y]

        return []


a = Solution()
print(a.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
print(a.findRedundantConnection([[1,2],[1,3],[2,3]]))
