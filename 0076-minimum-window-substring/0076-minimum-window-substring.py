from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
            
        # Dictionary to keep track of required counts of characters in t
        dict_t = Counter(t)
        required = len(dict_t)
        
        # Filtered list of characters in s that are present in t along with their indices
        # (Optimization: helps skip unnecessary characters in large strings)
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))
                
        l, r = 0, 0
        formed = 0
        window_counts = {}
        
        # Tuple format: (window_length, left_index, right_index)
        min_len = float("inf")
        min_window = ("", 0, 0)
        
        while r < len(filtered_s):
            char = filtered_s[r][1]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if window_counts[char] == dict_t[char]:
                formed += 1
                
            # Try and contract the window until it ceases to be desirable
            while l <= r and formed == required:
                char = filtered_s[l][1]
                
                # Save the smallest window
                start = filtered_s[l][0]
                end = filtered_s[r][0]
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    min_window = (s[start:end + 1], start, end)
                    
                window_counts[char] -= 1
                if window_counts[char] < dict_t[char]:
                    formed -= 1
                    
                l += 1
                
            r += 1
            
        return min_window[0] if min_len != float("inf") else ""