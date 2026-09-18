from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
            
        queue = deque([(beginWord, 1)])
        
        while queue:
            current_word, length = queue.popleft()
            
            if current_word == endWord:
                return length
                
            # Try changing each character position
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]
                    
                    if next_word in word_set:
                        word_set.remove(next_word)
                        queue.append((next_word, length + 1))
                        
        return 0