from collections import Counter

class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        n = len(target)
        sticker_counts = [Counter(s) for s in stickers]
        memo = {}
        
        def dfs(mask):
            if mask == 0:
                return 0
            if mask in memo:
                return memo[mask]
            
            res = float('inf')
            first_idx = 0
            while first_idx < n and not (mask & (1 << first_idx)):
                first_idx += 1
                
            target_char = target[first_idx]
            
            for sc in sticker_counts:
                if target_char not in sc:
                    continue
                
                next_mask = mask
                sc_copy = sc.copy()
                for i in range(n):
                    if (mask & (1 << i)) and target[i] in sc_copy and sc_copy[target[i]] > 0:
                        sc_copy[target[i]] -= 1
                        next_mask ^= (1 << i)
                        
                if next_mask != mask:
                    res = min(res, 1 + dfs(next_mask))
                    
            memo[mask] = res
            return res
            
        ans = dfs((1 << n) - 1)
        return ans if ans != float('inf') else -1