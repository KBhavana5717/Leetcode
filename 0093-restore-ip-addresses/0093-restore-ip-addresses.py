class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        n = len(s)
        
        # An IP address cannot be shorter than 4 digits or longer than 12 digits
        if n < 4 or n > 12:
            return res
            
        def backtrack(start_idx, path):
            # If we have 4 segments and used all characters, we found a valid IP
            if len(path) == 4:
                if start_idx == n:
                    res.append(".".join(path))
                return
                
            # Try taking 1, 2, or 3 digits for the current segment
            for length in range(1, 4):
                if start_idx + length > n:
                    break
                    
                segment = s[start_idx:start_idx + length]
                
                # Check validity:
                # 1. No leading zeros for segments with length > 1
                # 2. Value must be <= 255
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue
                    
                path.append(segment)
                backtrack(start_idx + length, path)
                path.pop()
                
        backtrack(0, [])
        return res