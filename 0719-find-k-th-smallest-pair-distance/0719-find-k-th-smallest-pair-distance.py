class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        low = 0
        high = nums[-1] - nums[0]
        
        while low < high:
            mid = (low + high) // 2
            count = 0
            left = 0
            
            # Count pairs with distance <= mid using two pointers
            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
                
            if count < k:
                low = mid + 1
            else:
                high = mid
                
        return low