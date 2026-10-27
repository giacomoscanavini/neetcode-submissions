class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Time complexity: Binary search of array with nested loop over piles O(n log(n))
        # Space complexity: Create fixed amount of variables O(1)
        l, r = 1, max(piles)+1
        output = 0
        while l < r:
            k = l + (r - l)//2
            t = 0
            for p in piles: t += p//k if p%k == 0 else p//k + 1

            if t <= h: 
                output = k
                r = k
            else: 
                l = k + 1
            
        return output