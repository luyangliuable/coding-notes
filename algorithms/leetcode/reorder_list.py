# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        # :type head: ListNode
        # :rtype: None Do not return anything, modify head in-place instead.
        # Beats 80%

        # At the very start need to make a and b head not a.next and b.next.next because b.next might be None
        # Had to check the solutions because I overcomplicated things
        # Forgot to check b.next.next in addition to b.next

        # Had trouble reversing the linkedlist
        # Had trouble merge two halfs of the linkedlist

        # Have two separate runs of linkedlists a and b
        # a will go to first half and b will reach the end

        # second half

        a = head
        b = head

        while b and b.next:
            a = a.next
            b = b.next.next

        # 2*a = b + 1
        # a = (b+1)//2

        s = a.next

        # Split first half from second half
        prev = a.next = None

        # Reverse the first half
        while s:
            tmp = s.next
            s.next = prev
            prev = s
            s = tmp


        # Merge second half with first half
        first = head
        # Seocnd half is reversed
        second = a

        first, second = head, prev
        # Merge first half with second half
        while first != None and second != None:
            tmp1, tmp2 = first.next, second.next

            # Swap first.next with second.next
            first.next = second
            second.next = tmp1

            # First will become old first.next
            # Second will become old second.next
            first, second = tmp1, tmp2

a = Solution()
