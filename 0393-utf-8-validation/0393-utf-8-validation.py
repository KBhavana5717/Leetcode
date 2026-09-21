class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        remaining_bytes = 0
        
        for num in data:
            # Keep only the least significant 8 bits
            num = num & 255
            
            if remaining_bytes == 0:
                # Determine how many bytes the character consists of
                if (num >> 7) == 0:
                    # 1-byte character (0xxxxxxx)
                    continue
                elif (num >> 5) == 6:
                    # 2-bytes character (110xxxxx)
                    remaining_bytes = 1
                elif (num >> 4) == 14:
                    # 3-bytes character (1110xxxx)
                    remaining_bytes = 2
                elif (num >> 3) == 30:
                    # 4-bytes character (11110xxx)
                    remaining_bytes = 3
                else:
                    return False
            else:
                # Must be a valid continuation byte (starts with 10xxxxxx)
                if (num >> 6) != 2:
                    return False
                remaining_bytes -= 1
                
        return remaining_bytes == 0