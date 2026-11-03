class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        words_exact = set(wordlist)
        words_cap = {}
        words_vowel = {}

        def devowel(word):
            return "".join('*' if c in 'aeiou' else c for c in word.lower())

        for w in wordlist:
            w_lower = w.lower()
            if w_lower not in words_cap:
                words_cap[w_lower] = w
            
            w_devowel = devowel(w)
            if w_devowel not in words_vowel:
                words_vowel[w_devowel] = w

        ans = []
        for q in queries:
            if q in words_exact:
                ans.append(q)
            elif q.lower() in words_cap:
                ans.append(words_cap[q.lower()])
            elif devowel(q) in words_vowel:
                ans.append(words_vowel[devowel(q)])
            else:
                ans.append("")
                
        return ans