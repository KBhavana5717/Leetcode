class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        chunks = 0
        max_val = 0
        for i, x in enumerate(arr):
            max_val = max(max_val, x)
            if max_val == i:
                chunks += 1
        return chunks