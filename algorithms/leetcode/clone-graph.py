class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        # Perform a depth first search on the node and for each node create a corresponding node.
        # Variables: current_node, current_new_node

        # Beats 95% of people !!!!!!! Yay!!!!!!!!
        
        return self.depthFirstSearch(node)

    def depthFirstSearch(self, node, v = {}):

        if node == None:
            return None

        c = Node(node.val, [])

        v[node] = c

        for n in node.neighbors:
            if n not in v: # Node visited
                c.neighbors.append(self.depthFirstSearch(n, v))
            else: # Node is visited
                c.neighbors.append(v[n])

        return c


    def breadthFirstSearch(self, node):
        v = []
        q = deque([node])


        while q:
            a = q.popleft()

            for n in a.neighbours:
                if n not in v:
                    v.append(n)
                    q.append(n)
