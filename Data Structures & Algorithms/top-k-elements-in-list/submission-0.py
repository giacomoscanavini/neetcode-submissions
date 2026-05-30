class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums: 
            hash_map[num] = hash_map.get(num, 0) + 1

        keys = hash_map.keys()
        values = hash_map.values()
        listOfTuples = sorted(zip(keys, values), key= lambda x:x[1], reverse=True)
        keys, values = zip(*listOfTuples)

        return list(keys[:k])
    
