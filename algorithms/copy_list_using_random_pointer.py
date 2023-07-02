# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        # :type head: Node
        # :rtype: Node
        # Beats 69%
        # Initially when created deepcopy, used a = r.next and each time made a. Forgot a is None

        m = {}

        # Traverse and create deepcopy of the original nodes.
        # Also create map of old and new corresponding nodes

        r = Node(0)

        a = r
        d = head


        while d:
            a.next = Node(d.val)
            if d not in m:
                m[d] = a.next

            d = d.next
            a = a.next

        # Traverse again linking random pointer using map this time

        d = head
        a = r.next

        while d and a:
            if d.random:
                a.random = m[d.random]

            d = d.next
            a = a.next

        return r.next
