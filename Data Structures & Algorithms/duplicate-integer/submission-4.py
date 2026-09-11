class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Complexity Time: O(n) to traverse nums
        # Complexity Memory: O(n) to create hash table
        hash_map = {}

        for num in nums: 
            hash_map[num] = hash_map.get(num, 0) + 1
            if hash_map[num] > 1: return True
        
        return False