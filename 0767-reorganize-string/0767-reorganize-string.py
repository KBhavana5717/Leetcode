class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        char, max_freq = count.most_common(1)[0]
        
        if max_freq > (len(s) + 1) // 2:
            return ""
            
        res = [None] * len(s)
        idx = 0
        
        for c, freq in count.most_common():
            for _ in range(freq):
                res[idx] = c
                idx += 2
                if idx >= len(s):
                    idx = 1
                    
        return "".join(res)