class Solution:
    def timeForPiles(self, piles: List[int], k: int) -> int:
        t = 0
        for pile in piles:
            t += int(pile / k)
            if pile % k > 0: t += 1
        return t

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Complexity Time: O(n * log(m)) where n is len(piles) and m is values for k
        # Complexity Memory: O(1)
        
        # Lower bound on k is 1 banana/hour
        # Upper bound on k is max(piles) banana/hour
        l, r = 1, max(piles)

        while l < r:
            m = l + (r - l) // 2
            t = self.timeForPiles(piles, m)

            if t <= h:
                # m works, but maybe a smaller speed also works
                r = m
            else:
                # m is too slow
                l = m + 1

        return l