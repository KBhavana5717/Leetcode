class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        left = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                left += 1
                i += 1
            else:
                # We need a pair of '))' for a '('
                # Check if the next character is also ')'
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    # Only one ')' found, we need to insert another ')'
                    res += 1
                    i += 1
                
                # Match with an available '('
                if left > 0:
                    left -= 1
                else:
                    # No '(' available, we need to insert an opening '('
                    res += 1
                    
        # Any remaining unmatched '(' needs two ')' each
        res += left * 2
        return res