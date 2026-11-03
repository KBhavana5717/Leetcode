class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def convert(string):
            if '.' not in string:
                return int(string), 1
            
            parts = string.split('.')
            integer_part = int(parts[0])
            decimal_part = parts[1]
            
            if '(' not in decimal_part:
                if not decimal_part:
                    return integer_part, 1
                length = len(decimal_part)
                return integer_part * (10**length) + int(decimal_part), 10**length
            
            non_rep, rep = decimal_part.split('(')
            rep = rep[:-1]
            
            l1 = len(non_rep)
            l2 = len(rep)
            
            num1 = integer_part * (10**l1) + int(non_rep or 0)
            den1 = 10**l1
            
            num2 = int(rep)
            den2 = (10**l2 - 1) * 10**l1
            
            import math
            total_den = den1 * den2 // math.gcd(den1, den2)
            total_num = num1 * (total_den // den1) + num2 * (total_den // den2)
            
            g = math.gcd(total_num, total_den)
            return total_num // g, total_den // g

        return convert(str(float(s))) == convert(str(float(t))) if len(s) <= 4 and len(t) <= 4 and '(' not in s and '(' not in t else convert(s) == convert(t)