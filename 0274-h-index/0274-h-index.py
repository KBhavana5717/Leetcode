class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        papers = [0] * (n + 1)
        
        for c in citations:
            papers[min(c, n)] += 1
            
        h = n
        count = papers[n]
        while h > count:
            h -= 1
            count += papers[h]
            
        return h