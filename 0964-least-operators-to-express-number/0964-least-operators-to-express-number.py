class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        memo = {}

        def dp(t):
            if t in memo:
                return memo[t]
            if t < x:
                # We can either use t additions of (x / x) or (x - x ...)
                # Cost for value 1 is 2, for value v is v * 2 - 1
                return min(t * 2 - 1, (x - t) * 2)

            k = 0
            curr = 1
            while curr < t:
                curr *= x
                k += 1

            if curr == t:
                return k - 1

            # curr is now x^k > t
            res = dp(t - curr // x) + k - 1
            
            # curr / x is x^(k-1) < t
            if curr - t < t:
                res = min(res, dp(curr - t) + k)

            memo[t] = res
            return res

        return dp(target)