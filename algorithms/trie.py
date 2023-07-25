# Implementing Trie using Trie and TrieNode classes
class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None]*26

        # property for representing the end of a word in the trie
        self.isEndOfWord = False

class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node with Null values
        return TrieNode()

    def _charToIndex(self,ch):

        """ private helper function
            Converts key current character into index
            only chracters a-z allowed in lowercase
        """

        return ord(ch)-ord('a')


    def insert(self,key):

        """ If word is already present in trie,
            just marks the leaf node to indicate
            If word isn't present then it creates the word in the trie
        """
        word = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if character is not present in trie
            if not word.children[index]:
                word.children[index] = self.getNode()
            word = word.children[index]

        # mark last node as leaf
        word.isEndOfWord = True

    def search(self, key):

        """ Search substring in the trie
            Returns true if substring is present
            in trie, else false
        """
        word = self.root
        length = len(key)
        level=0
        while level<length:
            index = self._charToIndex(key[level])
            if not word.children[index]:
                return False
            word = word.children[index]
            level+=1
        if level==length:
            return True
        else:
            return False


if __name__ == "__main__":
    trie = Trie()
    trie.insert("food")
    trie.insert("ood")
    trie.insert("od")
    print(trie.search("od"))
