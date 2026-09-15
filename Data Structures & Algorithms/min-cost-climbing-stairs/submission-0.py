class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Complexity Time: O(n)
        # Complexity Memory: O(1)
        '''
        # From 1 or 2 we directly arrive
        cost[2] = 3
        cost[1] = 2
        # From 0 we can't directly arrive so we either go to 1 or 2
        cost[0] = 1 + min(cost[1], cost[2])
        # Then we start from the step (0 or 1) with the min cost to ascend
        '''
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])