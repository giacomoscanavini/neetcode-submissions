class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Time complexity: Loop over the heights O(n)
        # Space complexity: Create fixed amount of variables O(1)
        max_water = 0
        
        i = 0
        j = len(heights) - 1
        while i < j:
            h = min(heights[i], heights[j])
            l = j - i
            max_water = max(max_water, l * h)

            if heights[i] >= heights[j]: j -= 1
            else: i += 1

        return max_water
            
