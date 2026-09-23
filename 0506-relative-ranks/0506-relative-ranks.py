class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        # Sort scores in descending order while keeping track of original indices
        sorted_scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        
        result = [""] * len(score)
        
        for rank, (orig_index, s) in enumerate(sorted_scores):
            if rank == 0:
                result[orig_index] = "Gold Medal"
            elif rank == 1:
                result[orig_index] = "Silver Medal"
            elif rank == 2:
                result[orig_index] = "Bronze Medal"
            else:
                result[orig_index] = str(rank + 1)
                
        return result