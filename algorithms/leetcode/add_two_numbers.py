from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        res = ListNode()
        h = res

        while l1 is not None or l2 is not None or c != 0:
            h.next = ListNode()
            h = h.next

            val = 0

            if c == 1:
                val += 1
                c = 0

            if l1:
                val += l1.val
                l1 = l1.next

            if l2:
                val += l2.val
                l2 = l2.next

            if val > 9:
                val -= 10
                c = 1

            h.val = val

        return res.next

if __name__ == '__main__':
    a = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    res = a.addTwoNumbers(l1, l2)

    while res != None:
        print(res.val)
        res = res.next
        

        
