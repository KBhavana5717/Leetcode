class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        diff = (sum_a - sum_b) // 2
        set_b = set(bobSizes)
        
        for x in aliceSizes:
            if x - diff in set_b:
                return [x, x - diff]