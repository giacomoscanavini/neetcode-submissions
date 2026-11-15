class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins))[::-1]:
            for val in range(1, amount + 1):
                if coins[i] <= val:
                    dp[val] += dp[val - coins[i]]
                    \

        return dp[amount]