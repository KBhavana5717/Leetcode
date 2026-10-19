class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        left, right = 0.0, 1.0
        
        while left < right:
            mid = (left + right) / 2
            count = 0
            p, q = 0, 1
            j = 1
            
            for i in range(n - 1):
                while j < n and arr[i] > mid * arr[j]:
                    j += 1
                count += n - j
                if j < n and arr[i] * q > p * arr[j]:
                    p, q = arr[i], arr[j]
                    
            if count == k:
                return [p, q]
            elif count < k:
                left = mid
            else:
                right = mid
                
        return []