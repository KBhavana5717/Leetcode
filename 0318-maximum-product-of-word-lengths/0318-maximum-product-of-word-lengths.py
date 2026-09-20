class Solution:
    def maxProduct(self, words: list[str]) -> int:
        n = len(words)
        masks = [0] * n
        lengths = [len(word) for word in words]
        
        # Precompute bitmasks for each word
        for i, word in enumerate(words):
            bitmask = 0
            for char in word:
                bitmask |= 1 << (ord(char) - ord('a'))
            masks[i] = bitmask
            
        max_prod = 0
        
        # Check every pair of words
        for i in range(n):
            for j in range(i + 1, n):
                if (masks[i] & masks[j]) == 0:
                    max_prod = max(max_prod, lengths[i] * lengths[j])
                    
        return max_prod