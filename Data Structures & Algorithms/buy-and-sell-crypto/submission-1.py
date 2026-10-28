class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time complexity: Loop over prices O(n)
        # Space complexity: Create fixed number of variables O(1)
        maxProfit = 0
        bestBuy = float('inf')
        i = 0
        j = len(prices)-1
        for i in range(len(prices)):
            if prices[i] < bestBuy: 
                bestBuy = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - bestBuy)
        
        return maxProfit
            
