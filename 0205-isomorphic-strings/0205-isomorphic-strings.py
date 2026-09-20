class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_to_t = {}
        map_t_to_s = {}
        
        for char_s, char_t in zip(s, t):
            # Check if char_s is already mapped to a different char_t
            if char_s in map_s_to_t and map_s_to_t[char_s] != char_t:
                return False
            # Check if char_t is already mapped to a different char_s
            if char_t in map_t_to_s and map_t_to_s[char_t] != char_s:
                return False
            
            # Establish the mapping
            map_s_to_t[char_s] = char_t
            map_t_to_s[char_t] = char_s
            
        return True