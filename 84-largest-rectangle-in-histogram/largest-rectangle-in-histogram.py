class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        ans = 0

        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0
                ans = max(ans, height * (i - left))

            stack.append(i)

        return ans