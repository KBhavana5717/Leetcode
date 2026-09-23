class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        length = len(n)
        candidates = set()
        
        # Edge cases: 10^length + 1 and 10^(length - 1) - 1
        candidates.add(10**length + 1)
        candidates.add(10**(length - 1) - 1)
        
        # Generate candidates from the prefix of the number
        prefix_len = (length + 1) // 2
        prefix = int(n[:prefix_len])
        
        for p in [prefix - 1, prefix, prefix + 1]:
            p_str = str(p)
            if length % 2 == 0:
                candidate = p_str + p_str[::-1]
            else:
                candidate = p_str + p_str[:-1][::-1]
            candidates.add(int(candidate))
            
        # Exclude the number itself
        candidates.discard(num)
        
        # Find the closest palindrome, with smaller number preferred on ties
        ans = None
        min_diff = float('inf')
        
        for cand in candidates:
            diff = abs(cand - num)
            if diff < min_diff or (diff == min_diff and cand < int(ans)):
                min_diff = diff
                ans = str(cand)
                
        return ans