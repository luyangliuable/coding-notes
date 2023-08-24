# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = []

        # Go through head and store each kth into arr and cut them

        d = head

        a.append(d)

        while True:
            breakflag = 0
            for _ in range(k):
                if d.next:
                    d = d.next
                else: # Not enough nodes
                    breakflag = 1
                    break

            if breakflag:
                break

            d.next = None

            a.append(d)

        r = ListNode()
        d2 = r

        def dfs(n, d2):
            if n is None:
                return

            dfs(n.next, d2)

            d2.next = ListNode(n.val)
            d2 = d2.next


        # Reverse every linkedlist and return it
        for n in a:
            dfs(n, d2)

        d = d.next if d.next != None else None

        while d:
            d2 = ListNode(d.val)

            d = d.next

        return r.next


