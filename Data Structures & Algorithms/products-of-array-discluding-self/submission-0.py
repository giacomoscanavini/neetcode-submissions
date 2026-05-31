class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Using left and right products
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0: 
                pass
            else:
                j = len(nums) - 1 - i
                left[i] = left[i-1] * nums[i-1]
                right[j] = right[j+1] * nums[j+1]

        for i in range(len(nums)):
            left[i] = left[i] * right[i] 
        return left
        # Complexity: O(n)
        # Memory: O(n)




        