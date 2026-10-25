class Solution:
    def trap(self, height: List[int]) -> int:
        # Time complexity: Loop over height O(n)
        # Space complexity: Create fixed number of variables O(1)
        i = 0
        j = len(height) - 1
        water = 0
        maxLeft, maxRight = height[i], height[j]

        while i < j:
            if maxLeft < maxRight: 
                i += 1
                maxLeft = max(maxLeft, height[i])
                water += maxLeft - height[i]

            else:
                j -= 1
                maxRight = max(maxRight, height[j])
                water += maxRight - height[j]

        return water