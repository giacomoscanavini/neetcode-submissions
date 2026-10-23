class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time complexity: 3 loop over nums O(n)
        # Space complexity: 3 arrays of length nums O(n)
        left_pref = [1] * len(nums)
        right_pref = [1] * len(nums)

        for i in range(1, len(nums)):
            left_pref[i] = left_pref[i - 1] * nums[i - 1]

        for i in range(len(nums)-1)[::-1]:
            right_pref[i] = right_pref[i + 1] * nums[i + 1]

        return [x * y for x,y in zip(left_pref, right_pref)]