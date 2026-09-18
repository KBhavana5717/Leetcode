class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
            
        # cuts[i] will store the minimum cuts for substring s[0:i+1]
        cuts = [i for i in range(n)]
        
        # is_palindrome[j][i] will be True if s[j:i+1] is a palindrome
        is_palindrome = [[False] * n for _ in range(n)]
        
        for i in range(n):
            min_cuts = i  # Maximum cuts needed is i (all single characters)
            for j in range(i + 1):
                # Check if s[j:i+1] is a palindrome
                if s[j] == s[i] and (i - j <= 2 or is_palindrome[j + 1][i - 1]):
                    is_palindrome[j][i] = True
                    
                    # If s[0:i+1] is a palindrome, 0 cuts are needed
                    if j == 0:
                        min_cuts = 0
                    else:
                        min_cuts = min(min_cuts, cuts[j - 1] + 1)
                        
            cuts[i] = min_cuts
            
        return cuts[n - 1]