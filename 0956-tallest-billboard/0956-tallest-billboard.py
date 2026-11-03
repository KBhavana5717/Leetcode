class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        dp = {0: 0}
        
        for r in rods:
            for d, s in list(dp.items()):
                # Add to the taller side
                dp[d + r] = max(dp.get(d + r, 0), s)
                # Add to the shorter side (or subtract difference)
                diff = abs(d - r)
                sum_val = s + min(d, r)
                dp[diff] = max(dp.get(diff, 0), sum_val)            
        return dp.get(0, 0)