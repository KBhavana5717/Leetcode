class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        if not s:
            return [""]

        current_level = {s}
        res = []
        found = False

        while current_level:
            next_level = set()
            for string in current_level:
                if isValid(string):
                    res.append(string)
                    found = True
            
            # If we found valid strings at this level, stop exploring further depths
            if found:
                return res
            
            # Generate next level by removing one parenthesis at a time
            for string in current_level:
                for i in range(len(string)):
                    if string[i] in ('(', ')'):
                        next_level.add(string[:i] + string[i+1:])
            
            current_level = next_level

        return res