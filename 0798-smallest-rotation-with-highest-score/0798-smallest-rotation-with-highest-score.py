class Solution:
    def bestRotation(self, nums: list[int]) -> int:
        n = len(nums)
        diff = [0] * (n + 1)
        
        for i, x in enumerate(nums):
            left = (i + 1) % n
            right = (i - x + n) % n
            
            if left <= right:
                diff[left] += 1
                diff[right + 1] -= 1
            else:
                diff[left] += 1
                diff[n] -= 1
                diff[0] += 1
                diff[right + 1] -= 1
                
        max_score = -1
        best_k = 0
        current_score = 0
        
        for k in range(n):
            current_score += diff[k]
            if current_score > max_score:
                max_score = current_score
                best_k = k
                
        return best_k