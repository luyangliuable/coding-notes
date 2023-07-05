class OldSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Can use kadane algorithm
        # Does not work
        r = 0

        d = set()
        curr = 0
        
        for i, c in enumerate(s):
            if c not in d:
                d.add(c)
                curr += 1
            else:
                d = set()
                r = max(r, curr)

                if ( i + 1 < len(s) and s[i+1] == s[i] ):
                    curr = 0
                else:
                    curr = 1


        r = max(curr, r)

        return r


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window algorithm
        # BEats 95%!!!! WOw!

        # Forgot to put +1 in r - l + 1 when determining max_l.
        # I guess if you have l = r you have a string or length 1 so yeah

        d = set()
        max_l = 0
        l = 0

        for r, c in enumerate(s):
            while c in d:
                # keep chipping away left until we are left with a window without any duplicates
                d.remove(s[l])
                l += 1

            d.add(c)
            max_l = max(r - l + 1, max_l)

        return max_l

a = Solution()
print(a.lengthOfLongestSubstring("abcabcbb"))
print(a.lengthOfLongestSubstring("aab"))
                

