class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # dp[i] stores the number of combinations to make up amount i
        dp = [0] * (amount + 1)
        dp[0] = 1  # Base case: there is 1 way to make an amount of 0 (using no coins)
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
                
        return dp[amount]