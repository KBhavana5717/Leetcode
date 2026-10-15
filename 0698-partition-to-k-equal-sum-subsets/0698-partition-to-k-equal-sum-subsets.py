class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
            
        target = total_sum // k
        nums.sort(reverse=True)
        
        if nums[0] > target:
            return False
            
        n = len(nums)
        visited = [False] * n

        def backtrack(index, k_prime, current_sum):
            if k_prime == 0:
                return True
            if current_sum == target:
                return backtrack(0, k_prime - 1, 0)
                
            for i in range(index, n):
                if not visited[i] and current_sum + nums[i] <= target:
                    visited[i] = True
                    if backtrack(i + 1, k_prime, current_sum + nums[i]):
                        return True
                    visited[i] = False
                    
                    # Optimization: if a bucket is empty and we fail, 
                    # further empty buckets will also fail.
                    if current_sum == 0:
                        break
                        
            return False

        return backtrack(0, k, 0)