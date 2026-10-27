class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Time complexity: Loop over heights and stack O(n)
        # Space complexity: create stack O(n)
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while len(stack) > 0 and (i == n or heights[stack[-1]] >= heights[i]):
                idx = stack.pop(-1)
                h = heights[idx]
                w = i if len(stack) == 0 else i - stack[-1] - 1
                maxArea = max(maxArea, h * w)

            stack.append(i)
        
        return maxArea