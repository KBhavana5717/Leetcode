class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        total_distance = 0
        n = len(nums)
        
        # Iterate through all 32 bit positions
        for i in range(32):
            ones = 0
            for num in nums:
                # Check if the i-th bit is set
                if (num >> i) & 1:
                    ones += 1
            
            zeros = n - ones
            # For each bit position, pairs with different bits contribute (zeros * ones)
            total_distance += zeros * ones
            
        return total_distance