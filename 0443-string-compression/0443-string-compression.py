class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0
        n = len(chars)
        
        while read < n:
            char = chars[read]
            count = 0
            
            # Count occurrences of the current repeating character group
            while read < n and chars[read] == char:
                read += 1
                count += 1
                
            # Write the character to the compressed position
            chars[write] = char
            write += 1
            
            # If the group length is greater than 1, append its digits individually
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
                    
        return write