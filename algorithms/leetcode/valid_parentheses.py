class Solution(object):
    def isValid(self, s):
        # :type s: str
        # :rtype: bool
        # Beats 59%
        # Notes:
        # Initially forgot to take into acount cases when the string is 1 characters long or less
        # Also forgot to take into account when the stack is not empty after popping everything meaning that there are still open parentheses
        # Forgot to take into account case when stack is empty when trying to pop

        if len(s) < 2:
            return False

        p = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []

        for l in s:
            if l in p:
                stack.append(p[l])
            else:
                if not stack or stack.pop() != l:
                    return False

        return len(stack) == 0 # No unmatched open symbols left

        

a = Solution()
print(a.isValid("()[]{}"))
print(a.isValid("(][]{}"))
print(a.isValid("(("))
