class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        # Step 1: Get the XOR sum of the two unique numbers (a ^ b)
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
            
        # Step 2: Find the rightmost set bit to distinguish between the two numbers
        rightmost_set_bit = xor_sum & -xor_sum
        
        # Step 3: Separate numbers into two groups and XOR them individually
        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num
                
        return [num1, num2]