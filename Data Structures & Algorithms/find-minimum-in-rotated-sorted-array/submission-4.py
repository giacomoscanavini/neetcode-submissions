class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Time complexity: Binary search of array O(logn)
        # Space complexity: Create fixed number of variables O(1)
        l, r = 0, len(nums) - 1
        while l < r: 
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return nums[r]