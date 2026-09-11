class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Complexity Time: 
        # Complexity Memory: 
        hash_map = {}

        for i, value in enumerate(nums):
            if hash_map.get(value, -1) == -1: 
                hash_map[target - value] = i

            else:
                return [hash_map[value], i]
            
            
                

        
        