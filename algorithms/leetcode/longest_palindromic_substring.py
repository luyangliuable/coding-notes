class Solution(object):
    def longestPalindrome(self, s):
        # :type s: str
        # :rtype: str
        # Finished in 20 minutes
        # Initially got confused that curr_len ends at n + 1 not n because range(n) ends at n-1
        # Initially put `k = n + curr_len - 1` instead of `k = j + curr_len - 1` got index out of range
        # Python string slicing for i to i+3 string is s[i: i + 3 + 1]

        n = len(s)

        l = 0

        a = [ [0 for _ in range(n)]  for _ in range(n)]

        r = ""

        # Every single string is it's own palindrome

        for c_i in range(n):
            a[c_i][c_i] = 1
            if 1 > l:
                l = 1
                r = s[c_i]


        # Check two same adjacent characters
        for c_i in range(n-1):
            if s[c_i] == s[c_i + 1]:
                # remember second index is always greater for bottom left half
                a[c_i][c_i + 1] = 1

                if 2 > l:
                    l = 2
                    r = s[c_i:c_i + 1 + 1]

                

        # Check for palindromes of length 3 or more
        for curr_len in range(3, n + 1):
            for j in range(n - curr_len + 1):
                # j is the last letter in the palindrome
                # k is the first letter in the palindrome
                k = j + curr_len - 1

                if s[j] == s[k] and a[j + 1][k - 1] == 1:
                    if curr_len > l:
                        l = curr_len
                        r = s[j:k+1]

                    a[j][k] = 1

        return r


    def backtrack(self, r):
        pass


    def print(self, r):
        for row in r:
            print('[', end=' ')
            for num in row:
                print(num, end=' ')
            print(']')


a = Solution()
print(a.longestPalindrome("babad"))
