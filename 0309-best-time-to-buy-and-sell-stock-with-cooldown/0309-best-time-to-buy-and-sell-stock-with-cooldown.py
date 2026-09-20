class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        
        # Initialize states for the first day
        hold = -prices[0]
        sold = 0
        cooldown = 0
        
        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            prev_cooldown = cooldown
            
            # Transition equations
            hold = max(prev_hold, prev_cooldown - price)
            sold = prev_hold + price
            cooldown = max(prev_cooldown, prev_sold)
            
        return max(sold, cooldown)