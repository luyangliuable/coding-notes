from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) < 2:
            return True

        # Convert preq into adjacency arr
        adj = [[] for _ in range(numCourses)]

        for p in prerequisites:
            dep = p[1]
            curr = p[0]

            adj[dep].append(curr)


        v2 = [False for _ in range(numCourses)]

        for i in range(numCourses):
            if not v2[i]:
                q = [i]

                v = [False for _ in range(numCourses)]

                while len(q) > 0:
                    a = q.pop()

                    if v[a]:
                        return False

                    v[a] = True
                    v2[a] = True

                    for n in adj[a]:
                        q.append(n)

        return True

if __name__ == '__main__':
    a = Solution()
    p = [[1,0],[0,1]]
    numCourses = 2
    print(a.canFinish(numCourses, p))

    numCourses2 = 2
    prerequisites = [[1,0]]
    print(a.canFinish(numCourses2, prerequisites))

    numCourses3 = 20
    prerequisites2 = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]

    print(a.canFinish(numCourses3, prerequisites2))

    numCourses4 = 2
    prerequisites3 = [[0,1]]

    print(a.canFinish(numCourses4, prerequisites3))
