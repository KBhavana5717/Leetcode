class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
        ones = [i for i, x in enumerate(arr) if x == 1]
        cnt = len(ones)
        
        if cnt == 0:
            return [0, len(arr) - 1]
        
        if cnt % 3 != 0:
            return [-1, -1]
            
        k = cnt // 3
        i1, i2 = 0, k
        j1, j2 = k - 1, 2 * k - 1
        m1, m2 = 2 * k, cnt - 1
        
        part_len = len(arr) - ones[m1]
        
        i, j, k = ones[i1], ones[i2], ones[m1]
        
        while k < len(arr):
            if arr[i] == arr[j] == arr[k]:
                i += 1
                j += 1
                k += 1
            else:
                return [-1, -1]
                
        return [i - 1, j]