class Solution:
    def numSpecialEquivGroups(self, words: list[str]) -> int:
        unique_groups = set()
        
        for word in words:
            # Separate characters by even and odd indices, then sort them
            even_chars = sorted(word[0::2])
            odd_chars = sorted(word[1::2])
            
            # Store as a tuple of sorted lists (tuples are hashable and can go into a set)
            unique_groups.add((tuple(even_chars), tuple(odd_chars)))
            
        return len(unique_groups)