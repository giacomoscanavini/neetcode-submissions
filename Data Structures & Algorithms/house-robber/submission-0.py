class Solution:
    def rob(self, nums: List[int]) -> int:
        # Complexity Time: O(n)
        # Complexity Memory: O(1)
        robFirst, robSecond = 0, 0
        for num in nums: 
            robFirst, robSecond = robSecond, max(num + robFirst, robSecond)
        return robSecond