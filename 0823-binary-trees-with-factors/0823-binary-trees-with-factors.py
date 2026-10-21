class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        arr.sort()
        dp = {x: 1 for x in arr}
        MOD = 10**9 + 7
        
        for i, x in enumerate(arr):
            for j in range(i):
                left = arr[j]
                if x % left == 0:
                    right = x // left
                    if right in dp:
                        dp[x] = (dp[x] + dp[left] * dp[right]) % MOD
                        
        return sum(dp.values()) % MOD