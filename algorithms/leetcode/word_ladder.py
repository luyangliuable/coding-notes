class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        # :type beginWord: str
        # :type endWord: str
        # :type wordList: List[str]
        # :rtype: int

        al = [ [] for _ in range(len(wordList))]

        for w1_i, w1 in enumerate(wordList):
            for w2_i, w2 in enumerate(wordList):
                # For every combination of wordlist

                d = 0
                # Check differ by a letter
                for i in range(len(i)):
                    if w1[i] != w2[i]:
                        d += 1

                if d == 1:
                    al[w1_i].append(w2_i)
                    al[w2_i].append(w1_i)

        def dijkstra(start):
            # Everything that is popped from min heap queue is already known
            # When dist[v] changes v inside the queue also changes so it needs to sift up the min heap

            d = [len(wordList) + 1 for _ in range(len( wordList ))]

            pred = [-1 for _ in range(len(wordList))]

            q = []


            def push(v):
                q.append(v)

                i = len(q) - 1

                # Sift up

                while i > 0 and q[(i-1)//2] > q[i]:
                    swap((i-1)//2, i)

            def pop():
                swap(0, -1)

                # Pop smallest value from heap which is q[0]
                r = q.pop()

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

                return r


            def swap(a, b):
                q[a], q[b] = q[b], q[a]

            push(start)
            d[start] = 0

            while len(q) > 0:
                u = pop()

                for v in al[u]:
                    if d[v] == len(wordList) + 1:
                        # Update minimum path to v since u is confirmed to be minimum path
                        d[v] = d[u] + 1
                        pred[v] = u
                        push(v)
                    
