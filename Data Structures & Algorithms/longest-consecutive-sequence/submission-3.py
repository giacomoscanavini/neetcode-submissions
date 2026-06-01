class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Using hash map
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums:
                # found start of a potential sequence
                length = 1
                while (num + length) in nums:
                    # sequence is extending
                    length += 1
                longest = max(length, longest)
        return longest
        # Complexity: O(n) even though the nested loop is present
        # Memory: O(n)
        
        
        