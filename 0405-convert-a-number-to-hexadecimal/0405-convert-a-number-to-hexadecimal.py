class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        chars = "0123456789abcdef"
        result = []
        
        # Handle 32-bit two's complement representation for negative numbers
        num &= 0xFFFFFFFF
        
        while num > 0:
            result.append(chars[num & 15])
            num >>= 4
            
        return "".join(reversed(result))
        