import bisect

class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # Sort by width ascending, and by height descending if widths are equal
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Find the Longest Increasing Subsequence based on the height
        dp = []
        for _, h in envelopes:
            idx = bisect.bisect_left(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
                
        return len(dp)