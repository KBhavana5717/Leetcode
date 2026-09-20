class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        # Map each word's reverse to its original index
        word_map = {word[::-1]: i for i, word in enumerate(words)}
        result = set()
        
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                s1, s2 = word[:j], word[j:]
                
                # If s1 is a palindrome, check if reverse(s2) exists in words
                if s1 == s1[::-1] and s2 in word_map and word_map[s2] != i:
                    result.add((word_map[s2], i))
                    
                # If s2 is a palindrome, check if reverse(s1) exists in words
                if s2 == s2[::-1] and s1 in word_map and word_map[s1] != i:
                    result.add((i, word_map[s1]))
                    
        return list(result)