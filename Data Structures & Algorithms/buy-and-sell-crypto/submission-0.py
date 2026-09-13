class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Complexity Time: O(n) to traverse the array
        # Complexity Memory: O(1) to create a fixed number of int
        best_profit = 0
        i, j = 0, 1
        while j <= len(prices) - 1:
            if prices[j] > prices[i]: 
                profit = prices[j] - prices[i]
                best_profit = max(profit, best_profit)
            else:
                i = j
            j += 1

        return best_profit