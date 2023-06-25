# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # :type list1: Optional[ListNode]
        # :type list2: Optional[ListNode]
        # :rtype: Optional[ListNode]
        # Beats 70%
        # Can use dummy data r for first node and return r.next


        r = ListNode(0)
        n = r

        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        while list1 != None and list2 != None:

            if list1.val <= list2.val:
                n.next = ListNode(list1.val)
                list1 = list1.next
            else:
                n.next = ListNode(list2.val)
                list2 = list2.next

            n = n.next

        if list1 is not None:
            n.next = list1
        elif list2 is not None:
            n.next = list2

        return r.next
