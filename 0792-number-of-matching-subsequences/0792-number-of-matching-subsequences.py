class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        from collections import defaultdict
        
        waiting = defaultdict(list)
        for word in words:
            waiting[word[0]].append(iter(word[1:]))
            
        count = 0
        for char in s:
            if char in waiting:
                bucket = waiting[char]
                del waiting[char]
                for it in bucket:
                    nxt = next(it, None)
                    if nxt:
                        waiting[nxt].append(it)
                    else:
                        count += 1
                        
        return count