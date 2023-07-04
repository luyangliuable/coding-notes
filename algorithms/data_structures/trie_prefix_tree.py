class TrieNode:
    def __init__(self):
        # Could use ord() and dictionary to implement c instead of a dict could be faster
        self.c = {}
        # self.c = [None for _ in range(25 + 1)]
        # self.r = 97
        self.end_of_word = 0


class Trie:
    def __init__(self):
        # Beats 80%
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        curr = self.root

        for w in word:
            # if not curr.c[ord(w) - 97]:
            #     curr.c[ord(w) - 97] = TrieNode()

            # curr = curr.c[ord(w) - 97]

            if w not in curr.c:
                curr.c[w] = TrieNode()

            curr = curr.c[w]

        curr.end_of_word = 1


    def search(self, word: str) -> bool:
        curr = self.root

        for w in word:
            # if not curr.c[ord(w) - 97]:
            #     return False

            # curr = curr.c[ord(w) - 97]

            if w not in curr.c:
                return False

            curr = curr.c[w]

        return True if curr.end_of_word else False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for w in prefix:
            # if not curr.c[ord(w) - 97]:
            #     return False

            # curr = curr.c[ord(w) - 97]
            if w not in curr.c:
                curr.c[w] = TrieNode()

            curr = curr.c[w]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
