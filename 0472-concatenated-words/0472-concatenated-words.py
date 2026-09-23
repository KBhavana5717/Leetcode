class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        word_set = set(words)
        result = []
        
        def can_form(word, memo):
            if word in memo:
                return memo[word]
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set and (suffix in word_set or can_form(suffix, memo)):
                    memo[word] = True
                    return True
            memo[word] = False
            return False

        # Sort words by length to ensure we only check shorter components
        words.sort(key=len)
        memo = {}
        
        for word in words:
            word_set.remove(word) # temporarily remove to avoid using itself
            if can_form(word, memo):
                result.append(word)
            word_set.add(word)
            
        return result