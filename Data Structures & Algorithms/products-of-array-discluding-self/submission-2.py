class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Complexity Time: O(n) to traverse the arrays
        # Complexity Memory: O(n) to create the arrays
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
            
            j = len(nums) - i - 1
            right[j] = right[j + 1] * nums[j + 1]

        for i in range(len(nums)):
            left[i] = left[i] * right[i]

        return left