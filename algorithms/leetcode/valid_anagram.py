class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in t:
            if char not in char_count:
                return False

            char_count[char] -= 1

            if char_count[char] < 0:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram('anagram', 'nagaram'))

