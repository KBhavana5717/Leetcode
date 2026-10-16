class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [0] * (n2 + 1)
        max_len = 0
        
        for i in range(1, n1 + 1):
            for j in range(n2, 0, -1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                    max_len = max(max_len, dp[j])
                else:
                    dp[j] = 0
                    
        return max_len