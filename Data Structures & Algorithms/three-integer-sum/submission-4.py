class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Complexity Time: O(n^2) for the nested loop 
        # Complexity Memory: O(3 * m) to create the output list with m unique triplets        
        nums = sorted(nums)

        triplets = []
        for i in range(0, len(nums)-2):
            value = nums[i]
            if i > 0 and nums[i] == nums[i - 1]: continue
            if value > 0: break

            j, k = i+1, len(nums) - 1
            while j < k:
                zero = value + nums[j] + nums[k]
                if zero < 0:
                    j += 1
                elif zero > 0:
                    k -= 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return triplets
        