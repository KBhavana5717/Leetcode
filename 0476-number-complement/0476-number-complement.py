class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        while mask <= num:
            mask <<= 1
        
        # XORing num with (mask - 1) flips all bits up to the highest bit of num
        return num ^ (mask - 1)