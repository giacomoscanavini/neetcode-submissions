class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time complexity: Loop over all nums in set O(n)
        # Space complexity: Create a set of nums O(n)
        nums = set(nums)
        current_streak, longest_streak = 0, 0

        for n in nums:
            if n-1 in nums: continue
            else:
                current_streak = 1
                while n+1 in nums:
                    current_streak += 1
                    n += 1
                longest_streak = max(longest_streak, current_streak)

        return longest_streak

