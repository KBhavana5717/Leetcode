from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        freq = Counter(s)
        
        # Step 2: Sort characters primarily by frequency (descending), 
        # and secondarily by character itself if frequencies are equal
        sorted_chars = sorted(freq.keys(), key=lambda x: (-freq[x], x))
        
        # Step 3: Build the result string by repeating each character by its frequency
        return "".join(char * freq[char] for char in sorted_chars)