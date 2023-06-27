# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        # :type head: ListNode
        # :type n: int
        # :rtype: ListNode
        # Beats 60%
        # This is pretty simple just need to think like real life
        # half to instances of the same linkedlist head. Linkedlist a next() n times, then next() both till one reach the end.
        # Remove Linkedlist b.next and make it b.next.next

        # Return d.next not head because the result might be [] returning head won't ever return that
        # for _ in range(n) and while n > 0: n-=1 is the same
        # don't have to l = d.next because math

        d = ListNode(0, head)
        l = d
        r = head

        for _ in range(n):
            if r:
                r = r.next
            else:
                # LinkedList not long enough
                return head

        while r and l:
            l = l.next
            r = r.next

        if l and l.next:
            l.next = l.next.next

        return d.next
