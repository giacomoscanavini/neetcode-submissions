class Solution:
    def rob(self, nums):
        # Complexity Time: O(n) to traverse the array
        # Complexity Memory: O(1)
        return max(self.rob_sub(nums[:-1]), 
                   self.rob_sub(nums[1:]), 
                   self.rob_sub([nums[-1]] + nums[:-2]))

    def rob_sub(self, nums_sub):
        robFirst, robSecond = 0, 0
        for num in nums_sub:
            robFirst, robSecond = robSecond, max(robFirst + num, robSecond)
        return robSecond