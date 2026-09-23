class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # Dictionary to store the first occurrence index of a remainder
        # Initialize with remainder 0 at index -1 to handle subarrays starting from index 0
        remainder_map = {0: -1}
        current_sum = 0
        
        for i, num in enumerate(nums):
            current_sum += num
            
            # If k is specified, take the modulo
            remainder = current_sum % k if k != 0 else current_sum
            
            if remainder in remainder_map:
                # Check if the subarray length is at least 2
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                # Store the first time this remainder appears
                remainder_map[remainder] = i
                
        return False