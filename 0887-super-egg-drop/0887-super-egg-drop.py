class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [0] * (k + 1)
        m = 0
        while dp[k] < n:
            m += 1
            for x in range(k, 0, -1):
                dp[x] = dp[x] + dp[x - 1] + 1
        return m