class Solution:
    def trap(self, height: List[int]) -> int:
        # Time complexity: Loops over height O(n)
        # Space complexity: Create a fixed number of arrays O(n)
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n
        
        max_prefix = 0
        for i in range(n): 
            max_prefix = max(max_prefix, height[i])
            prefix[i] = max_prefix

        max_suffix = 0
        for j in range(n)[::-1]: 
            max_suffix = max(max_suffix, height[j])
            suffix[j] = max_suffix

        water = 0
        for i, (l, r) in enumerate(zip(prefix, suffix)):
            water += min(l, r) - height[i]

        return water