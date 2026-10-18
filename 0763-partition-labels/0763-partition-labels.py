class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurrence = {c: i for i, c in enumerate(s)}
        res = []
        start = 0
        end = 0
        
        for i, c in enumerate(s):
            end = max(end, last_occurrence[c])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
                
        return res