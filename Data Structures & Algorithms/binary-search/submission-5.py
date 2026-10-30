class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time complexity: Binary search of an array O(logn)
        # Space complexity: Create fixed number of variables O(1)
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r + l)//2
            if nums[m] < target: l = m + 1
            elif nums[m] > target: r = m - 1
            else: return m
        
        return -1