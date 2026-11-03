class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        res = []
        n = len(arr)
        
        for x in range(n, 1, -1):
            idx = arr.index(x)
            if idx == x - 1:
                continue
            if idx != 0:
                res.append(idx + 1)
                arr[:idx + 1] = arr[:idx + 1][::-1]
            res.append(x)
            arr[:x] = arr[:x][::-1]
            
        return res