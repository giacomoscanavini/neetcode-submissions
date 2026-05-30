class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums: 
            hash_map[num] = hash_map.get(num, 0) + 1

        # Using bucketSort
        buckets = [None] * (len(nums) + 1)
        for key,value in hash_map.items():
            if buckets[value] is None:
                buckets[value] = [key]
            else:
                buckets[value].append(key)

        top_k = []
        for i in range(len(buckets))[::-1]:
            if buckets[i] is not None:
                top_k = top_k + buckets[i]

                if len(top_k) == k:
                    break
        return top_k




    
