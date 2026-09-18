class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        memo = {}
        
        def dfs(sub: str) -> list[str]:
            if sub in memo:
                return memo[sub]
            if not sub:
                return [""]
                
            res = []
            for i in range(1, len(sub) + 1):
                word = sub[:i]
                if word in word_set:
                    # Recursively get sentences for the remaining substring
                    next_sentences = dfs(sub[i:])
                    for next_sentence in next_sentences:
                        if next_sentence:
                            res.append(word + " " + next_sentence)
                        else:
                            res.append(word)
                            
            memo[sub] = res
            return res
            
        return dfs(s)