class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        for k in range(1, n + 1):
            if n % k != 0:
                continue
                
            sortable = True
            prev_max = -float('inf')
            
            for i in range(0, n, k):
                sub = nums[i:i + k]
                
                # Check if 'sub' can be rotated into a sorted array (at most 1 drop)
                drops = 0
                for j in range(k):
                    if sub[j] > sub[(j + 1) % k]:
                        drops += 1
                        
                if drops > 1:
                    sortable = False
                    break
                    
                curr_min = min(sub)
                curr_max = max(sub)
                
                # Ensure the current block's minimum is >= the previous block's maximum
                if prev_max > curr_min:
                    sortable = False
                    break
                    
                prev_max = curr_max
                
            if sortable:
                total_sum += k
                
        return total_sum