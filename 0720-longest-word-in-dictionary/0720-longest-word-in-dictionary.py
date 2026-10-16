class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)
        longest = ""
        
        for word in words:
            # Check if all prefixes of the word are present in the set
            if all(word[:i] in word_set for i in range(1, len(word))):
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
                    
        return longest