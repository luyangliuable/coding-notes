class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:



class TrieNode:
    def __init__(self):
        self.e = [0 for _ in range(26)]
