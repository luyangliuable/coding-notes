# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        # :type head: ListNode
        # :rtype: ListNode
        # Store current one in a tmp arr, swap current one and next one. Tn
        # Beats 44%
        # Confused because curr how the while curr works
        # Basically grab the head of curr each time and make reversing point it it.
        # Each loop reversing contains the currently reversed list so far

        d = ListNode(0, head)

        curr = d.next

        # reversing contains the reversing linkedlist
        # First one's next will be None
        reversing = None

        while curr:
            # temporarily store current one
            tmp = curr.next

            # Temporarily store the head of curr and link it to reversing
            curr.next = reversing

            # Make reversing equal to the head of curr and that lins to the prev the reversing
            reversing = curr

            # Make curr the previous curr.next
            curr = tmp

        return reversing

    def traverse(self, head):
        d = ListNode(0, head)
        a = d.next

        while a:
            print(a.val, end=' ')

            if a.next:
                print('-> ')

            a = a.next


a = Solution()
t = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
b = ListNode(0, t)
c = a.reverseList(t)
# print(t.val, t.next.val, t.next.next.val)
a.traverse(c)
