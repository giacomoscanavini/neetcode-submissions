class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Time complexity: Loop over nums O(n)
        # Space complexity: Create fixed number of variables O(1)
        # n = len(nums)

        # Edge cases

        # Main code
        windowMax, windowMin = 1, 1
        maxProd = nums[0]
        for num in nums:
            temp = windowMax * num
            windowMax = max(num, windowMax * num, windowMin * num)
            windowMin = min(num, temp, windowMin * num)
            maxProd = max(maxProd, windowMax)

        return maxProd