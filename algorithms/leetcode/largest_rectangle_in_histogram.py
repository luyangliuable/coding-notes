import sys

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Beats 26%
        # Hard
        # Lots of silly mistakes
        # Issue with not sure what to do when popping bars when the next height is smaller than the top of the stack
        # In that I wasn't sure should we calculate the area of indivual bars and ones after it and realised there is a geenious solution
        # Forgot to calculate width as i-j and len(heights) - start instead of just j and start which is not right
        s = []
        r = 0

        for i, h in enumerate(heights):
            start = i
            while len(s) > 0 and s[-1][1] > h:
                j, height = s.pop()

                r = max(height*(i-j), r)

                start = j

            s.append([start, h])

        while s:
            start, h = s.pop()

            length = len(heights) - start

            r = max(length*h, r)

        return r
