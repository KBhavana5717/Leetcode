from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        out = {}
        
        # Unique character identifiers for specific numbers
        out[0] = count['z']
        out[2] = count['w']
        out[4] = count['u']
        out[6] = count['x']
        out[8] = count['g']
        
        # Derived character identifiers using already found digits
        out[1] = count['o'] - out[0] - out[2] - out[4]
        out[3] = count['h'] - out[8]
        out[5] = count['f'] - out[4]
        out[7] = count['s'] - out[6]
        out[9] = count['i'] - out[5] - out[6] - out[8]
        
        # Build the final sorted string of digits
        result = []
        for digit in range(10):
            result.append(str(digit) * out[digit])
            
        return "".join(result)