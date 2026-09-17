from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
            
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result = []
        
        # We only need to iterate up to word_len offsets because any other 
        # starting index would just be covered by one of these residue offsets.
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            words_used = 0
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] += 1
                    words_used += 1
                    
                    # If there are too instances of a word, shrink from the left
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        words_used -= 1
                        left += word_len
                        
                    # If we matched all words correctly, record the starting index
                    if words_used == num_words:
                        result.append(left)
                else:
                    # Reset window if an invalid word is encountered
                    current_count.clear()
                    words_used = 0
                    left = right
                    
        return result