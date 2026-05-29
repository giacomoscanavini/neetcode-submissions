class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, num in enumerate(nums): 
            need = target - num
            if need in hash_map.keys():
                return [hash_map[need], index]
            else:
                hash_map[num] = index