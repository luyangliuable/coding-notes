class Solution(object):
    def partitionLabels(self, s):
        # :type s: str
        # :rtype: List[int]
        # Beats 89.1%
        # Initially forgot and made i start at 1 which doesn't take into account cases the first str can be a substr

        # Diction containg the last string occurence in s
        c = {}

        for i in range(len(s)):
            c[s[i]] = i

        res = []

        curr = 1
        i = 0
        goal = c[s[0]]

        # Edge case len(s) == 1 or 0 for better efficiency
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0

        while i < len(s):
            goal = max(goal, c[s[i]])

            if goal == i:
                res.append(curr)
                curr = 0

            curr += 1
            i += 1

        return res


a = Solution()
print(a.partitionLabels("ababcbacadefegdehijhklij"))
