class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time complexity: loop over nums + loop over buckets O(n)
        # Space complexity: hash map + bucket O(n)
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        # Bucket sort
        buckets = [None] * (len(nums) + 1)
        for key,val in frequency_map.items():
            if buckets[val] == None: buckets[val] = [key]
            else: buckets[val].append(key)

        # Top-k
        top_k = []
        for bucket in buckets[::-1]:
            if len(top_k) == k: break
            else:
                if bucket == None: continue
                else: top_k += bucket

        return top_k