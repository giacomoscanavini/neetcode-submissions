class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tuples = []
        nums = sorted(nums)

        for i,num in enumerate(nums):
            if num > 0: break # All remaining are positive, no way to get 0
            if i > 0 and num == nums[i - 1]: continue # Same starting number
            
            # Two pointers
            j = i + 1
            k = len(nums) - 1
            while j < k: 
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum == 0: 
                    tuples.append([nums[i], nums[j], nums[k]])
                    
                    # Advance j index, make sure it is not identical
                    j += 1
                    while nums[j] == nums[j-1] and j < k: j += 1
                
                elif threeSum < 0:
                    j += 1 # Sum is too low, need higher number
                
                else:
                    k -= 1 # Sum is too high, need lower number

        return tuples



        