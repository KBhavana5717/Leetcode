class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        # Iterate through 1-indexed positions
        for i in range(1, n + 1):
            if n % i == 0:
                # Add the square of the element at 1-indexed position `i` (0-indexed `i - 1`)
                total_sum += nums[i - 1] * nums[i - 1]
                
        return total_sum