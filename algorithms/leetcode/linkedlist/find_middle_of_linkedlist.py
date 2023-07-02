class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "["+str( self.val )+"]"

class Solution(object):
    def middle(self, head):
        # Initially got it wrong

        a = head
        b = head

        while b and b.next:
            a = a.next
            b = b.next.next

        return a


# 1 -> 2 -> 4
test = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))

a = Solution()
print(a.middle(test))
