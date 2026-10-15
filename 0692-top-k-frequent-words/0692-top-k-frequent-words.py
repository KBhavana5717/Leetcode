from collections import Counter

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        # Sort by frequency descending, then by word ascending
        sorted_words = sorted(count.keys(), key=lambda w: (-count[w], w))
        return sorted_words[:k]