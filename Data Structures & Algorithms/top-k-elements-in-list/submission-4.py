class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Complexity Time: O(n)
        # Complexity Memory: O(n) to create the hash_map and arrays
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        
        # Using bucket sort
        buckets = [None] * (len(nums) + 1)
        for num,freq in hash_map.items():
            if buckets[freq] is None: 
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)

        top_k = []
        for bucket in buckets[::-1]:
            if bucket is None: 
                pass
            else:
                top_k += bucket
                if len(top_k) == k: return top_k