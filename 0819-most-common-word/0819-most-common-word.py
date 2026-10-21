class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        import re
        from collections import Counter
        
        banned_set = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        
        counts = Counter(w for w in words if w not in banned_set)
        
        return counts.most_common(1)[0][0]