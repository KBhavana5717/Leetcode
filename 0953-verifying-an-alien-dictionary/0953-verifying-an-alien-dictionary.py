class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_map = {char: i for i, char in enumerate(order)}
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            for j in range(len(word1)):
                # If we run out of letters in the second word, and the first is longer, it's invalid
                if j == len(word2):
                    return False
                
                if word1[j] != word2[j]:
                    if order_map[word1[j]] > order_map[word2[j]]:
                        return False
                    break
            else:
                # If we finished the loop without breaking, word1 is a prefix of word2 (e.g., "apple" and "app")
                if len(word1) > len(word2):
                    return False
                    
        return True