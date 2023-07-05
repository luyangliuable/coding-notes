# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.c = capacity # capacity
        self.n = 0 # length of linkedlist
        self.m = {} # map of existing
        self.l = None # linkedlist


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        a = self.l

        if self.n + 1 <= self.c:
            while a:
                if a 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
