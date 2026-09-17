class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_exponent = False
        seen_dot = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in "+-":
                # A sign is only valid at the beginning or right after an exponent ('e' or 'E')
                if i > 0 and s[i - 1] not in "eE":
                    return False
            elif char in ".":
                # A dot cannot appear if we already saw a dot or an exponent
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            elif char in "eE":
                # An exponent cannot appear if we already saw one, or if we haven't seen any digit yet
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False  # Reset to ensure digits follow the exponent
            else:
                return False
                
        return seen_digit