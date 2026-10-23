class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for n in nums:
            if not hash_map.get(n, 0): 
                hash_map[n] = 1
            else:
                return True

        return False