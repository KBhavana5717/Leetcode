class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        s = set(arr)
        n = len(arr)
        max_len = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]
                l = 2
                while a + b in s:
                    a, b = b, a + b
                    l += 1
                    max_len = max(max_len, l)
                    
        return max_len if max_len >= 3 else 0