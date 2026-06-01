class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Using sorting
        if len(nums) == 0: return 0
        else:
            nums = sorted(set(nums))
            longest = 1
            current = 1

            def checkout(longest, current):
                if current > longest:
                    longest = current # overwrite
                return longest

            for i in range(1, len(nums)):
                if nums[i] - nums[i-1] == 1:
                    # continue sequence
                    current += 1
                    print(f"{nums[i]} - {nums[i-1]} = {nums[i]-nums[i-1]}, current = {current}")
                else:
                    # new sequence
                    longest = checkout(longest, current)
                    # reset sequence
                    current = 1
                    print(f"New sequence starting with {nums[i]}: {nums[i]} - {nums[i-1]} = {nums[i]-nums[i-1]}")
                    print(f"Longest = {longest}")
                
                if i == len(nums) - 1: 
                    longest = checkout(longest, current)
            
            return longest
