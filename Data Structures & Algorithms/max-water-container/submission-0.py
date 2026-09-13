class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Complexity Time: 
        # Complexity Memory: 
        max_A = 0
        i, j = 0, len(heights) - 1
        while i < j:
            w = j - i
            h = min(heights[i], heights[j])
            A = w * h
            if A > max_A: 
                max_A = A

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return max_A



        