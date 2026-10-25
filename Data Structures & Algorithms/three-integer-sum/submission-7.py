class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time complexity: sorting is O(n log(n)) + nested loop O(n^2)
        # Space complexity: create sorted list O(n) and output list O(n)
        nums = sorted(nums)
        output = []

        i = 0
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            if nums[i] > 0: break

            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                value = nums[l] + nums[r]
                if value < target: l += 1
                elif value > target: r -= 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) - 1 and nums[l] == nums[l-1]: l += 1

        return output