# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):

        # Perform a breadth first search on the node and for each node create a corresponding node.
        # Breadth first search because it is easier
        # Variables: current_node, current_new_node
        # TODO: brush up breadth first search
