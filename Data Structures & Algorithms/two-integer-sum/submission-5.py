class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time complexity: loop over elements of nums O(n)
        # Space complexity: create hash map O(n)
        hash_map = {}
        for i,n in enumerate(nums):
            diff = target - n
            if n in hash_map.keys(): 
                return [hash_map[n], i]
            else:
                hash_map[diff] = i

