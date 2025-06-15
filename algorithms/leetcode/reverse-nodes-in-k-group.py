class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode | None:
        r = ListNode()

        self.dfs(head, r)

        return r.next

    def dfs(self, node: ListNode | None, h: ListNode) -> ListNode | None:

        if node is not None:
            a = self.dfs(node.next, h)
            print(node.val)
            return a

        return ListNode(0, None)

    def get_kth_node(self, n, head):
        r = head

        while r and n > 0:
            r = r.next
            n -= 1

        return r



if __name__ == '__main__':
     a = Solution()

     head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

     res = a.reverseKGroup(head, 1)

     while res is not None:
         print(res.val)
         res = res.next

