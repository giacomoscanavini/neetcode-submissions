class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Complexity Time: O(n) to traverse the array
        # Complexity Memory: O(n) to create the set
        
        # Note that converting to set allows for O(1) time lookups
        set_nums = set(nums) 
        l_longest = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                l_current = 1
                while num + l_current in set_nums:
                    l_current += 1
                l_longest = max(l_current, l_longest)
        return l_longest