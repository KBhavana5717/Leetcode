class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Initialize states for up to two transactions
        hold1, release1 = float('-inf'), 0
        hold2, release2 = float('-inf'), 0
        
        for price in prices:
            hold1 = max(hold1, -price)
            release1 = max(release1, hold1 + price)
            hold2 = max(hold2, release1 - price)
            release2 = max(release2, hold2 + price)
            
        return release2