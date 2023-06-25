import heapq

class OldSolution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        # :type beginWord: str
        # :type endWord: str
        # :type wordList: List[str]
        # :rtype: int
        # Ran out of time due to time complexity

        s = -1
        e = -1

        for i in range(len(wordList)):
            if wordList[i] == beginWord:
                s = i
            elif wordList[i] == endWord:
                e = i

        if s == -1:
            wordList.append(beginWord)
            s = len(wordList) - 1

        if e == -1:
            return 0

        al = [ [] for _ in range(len(wordList))]

        for w1_i in range(len( wordList )):
            for w2_i in range(w1_i, len( wordList )):
                # For every combination of wordlist
                w1 = wordList[w1_i]
                w2 = wordList[w2_i]

                d = 0
                # Check differ by a letter
                for i in range(len(w1)):
                    if w1[i] != w2[i]:
                        d += 1

                if d == 1:
                    al[w1_i].append(w2_i)
                    al[w2_i].append(w1_i)


        d = [len(wordList) + 1 for _ in range(len( wordList ))]
        pred = [-1 for _ in range(len(wordList))]

        def dijkstra(start):
            # Everything that is popped from min heap queue is already known
            # When dist[v] changes v inside the queue also changes so it needs to sift up the min heap

            def push(v):
                q.append(v)

                i = len(q) - 1

                # Sift up

                while i > 0 and q[(i-1)//2] > q[i]:
                    swap((i-1)//2, i)

                # return final index of new value v
                return i


            def pop():
                swap(0, -1)

                # Pop smallest value from heap which is q[0]
                o = q.pop()

                # sink down 0th value of q
                i = 0

                while True:
                    s = i
                    l = i*2 + 1
                    r = 2*i + 2

                    if l < len(q) and q[l] < q[s]:
                        s = l

                    if r < len(q) and q[r] < q[s]:
                        s = r

                    if i == s:
                        break

                    swap(i, s)

                    i = s

                return o


            def swap(a, b):
                q[a], q[b] = q[b], q[a]

            # def update(v, idx):
            #     if v not in map:
            #         map[v] = idx
            #         return

            #     map[v] = idx

            q = [(0, start)]

            d[start] = 0


            while len(q) > 0:
                dist_u, u = heapq.heappop(q)

                if dist_u != d[u]:  # Skip outdated copies of u in the heap
                        continue

                for v in al[u]:
                    if d[v] == len(wordList) + 1:
                        # Update minimum path to v since u is confirmed to be minimum path
                        d[v] = dist_u + 1
                        pred[v] = u

                        heapq.heappush(q, (d[v], v))  

            return d

        dijkstra(s)

        return d[e] + 1 if d[e] < len(wordList) + 1 else 0

import collections
from collections import deque

class Solution:
    def ladderLength(self, beginword, endword, wordlist):
        if endword not in wordlist:
            return 0

        nei = collections.defaultdict(list)

        # Construct a hashtable/dict with wildcard strings matching the word missing a letter. Represents the graph
        # Each nodes based on checking dict for every missing letter
        wordlist.append(beginword)
        for word in wordlist:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        # Check word in visit is O(1) if set
        visit = set([beginword])

        # queue
        q = deque([beginword])

        res = 1

        # Run breadth first each, each while loop is one layer.
        while q:
            # Where there are still layer left to traverse in bfs

            for i in range(len(q)):
                # For every remaining nodes from last layer

                # FILO
                word = q.popleft()

                if word == endword:
                    # If word identified at current layer return it
                    return res
                for j in range(len(word)):
                    # For every adjacent node (word)
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiword in nei[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)

                            # push to queue
                            q.append(neiword)
            # +1 layers into the search
            res += 1
        return 0
                    

a = Solution()
print(a.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
# print(a.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"]))
