class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0
        k = 1
        while n > k * (k - 1) // 2:
            if (n - k * (k - 1) // 2) % k == 0:
                ans += 1
            k += 1
        return ans