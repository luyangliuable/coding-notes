import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        # :type lists: List[ListNode]
        # :rtype: ListNode
        # Beats only 5%
        # Initally forgot and return r not dummy.next
        # 

        dummy = ListNode(0)
        r = dummy

        while True:
            min = -1
            min_val = sys.maxsize

            for i in range( len( lists ) ):
                if lists[i] and min_val > lists[i].val:
                    min = i
                    min_val = lists[i].val

            if min == -1:
                break

            r.next= ListNode(min_val)

            r = r.next

            lists[min] = lists[min].next

        return dummy.next
