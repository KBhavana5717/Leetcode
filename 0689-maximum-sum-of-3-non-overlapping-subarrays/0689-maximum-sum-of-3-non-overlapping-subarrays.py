class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        # Calculate the sum of all windows of length k
        w_sums = [sum(nums[:k])]
        for i in range(k, n):
            w_sums.append(w_sums[-1] - nums[i - k] + nums[i])
            
        m = len(w_sums)
        left = [0] * m
        best = 0
        for i in range(m):
            if w_sums[i] > w_sums[best]:
                best = i
            left[i] = best
            
        right = [0] * m
        best = m - 1
        for i in range(m - 1, -1, -1):
            if w_sums[i] >= w_sums[best]:
                best = i
            right[i] = best
            
        max_sum = 0
        ans = []
        for j in range(k, m - k):
            l = left[j - k]
            r = right[j + k]
            total = w_sums[l] + w_sums[j] + w_sums[r]
            if total > max_sum:
                max_sum = total
                ans = [l, j, r]
                
        return ans