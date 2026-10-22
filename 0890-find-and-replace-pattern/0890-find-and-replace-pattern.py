class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        def get_match_pattern(s: str) -> list[int]:
            mapping = {}
            res = []
            for char in s:
                if char not in mapping:
                    mapping[char] = len(mapping)
                res.append(mapping[char])
            return res
        
        pattern_norm = get_match_pattern(pattern)
        return [word for word in words if get_match_pattern(word) == pattern_norm]