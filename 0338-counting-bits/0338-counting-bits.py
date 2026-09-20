class Solution:
    def countBits(self, n: int) -> list[int]:
        # Initialize an array of size n + 1 with zeros
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # ans[i >> 1] gets the count for i / 2, and (i & 1) adds 1 if i is odd
            ans[i] = ans[i >> 1] + (i & 1)
            
        return ans