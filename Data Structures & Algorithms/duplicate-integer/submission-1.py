class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Using a set
        if len(set(nums)) < len(nums):
            return True
        else:
            return False