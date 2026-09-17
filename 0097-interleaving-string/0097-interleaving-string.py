class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        r, c = len(s1), len(s2)
        
        if r + c != len(s3):
            return False
            
        dp = [False] * (c + 1)
        
        for i in range(r + 1):
            for j in range(c + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
                    
        return dp[c]