class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time complexity: loop over all numbers in nums O(n)
        # Space complexity: creating the set of nums O(n)
        nums = set(nums)
        current_streak = 0
        longest_streak = 0
        for n in nums:
            if n - 1 in nums: 
                continue
            else:
                current_streak = 1
                k = n + 1
                while k in nums:
                    current_streak += 1
                    k += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak