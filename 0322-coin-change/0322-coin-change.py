class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Initialize dp array with infinity for all amounts up to 'amount'
        dp = [float('inf')] * (amount + 1)
        
        # Base case: 0 coins are needed to make amount 0
        dp[0] = 0
        
        # Build up the dp table from 1 to amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return dp[amount] if dp[amount] != float('inf') else -1