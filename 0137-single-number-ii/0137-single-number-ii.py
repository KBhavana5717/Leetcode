class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            # Update ones: add num if it's not already in twos
            ones = (ones ^ num) & ~twos
            # Update twos: add num if it's not already in ones
            twos = (twos ^ num) & ~ones
            
        return ones