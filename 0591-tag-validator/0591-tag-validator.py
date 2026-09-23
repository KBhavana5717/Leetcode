class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        n = len(code)
        
        while i < n:
            # If code has content outside the outermost tag, it's invalid
            if i > 0 and not stack:
                return False
                
            if code.startswith("<![CDATA[", i):
                j = code.find("]]>", i)
                if j == -1:
                    return False
                i = j + 3
            elif code.startswith("</", i):
                j = code.find(">", i)
                if j == -1:
                    return False
                tag = code[i+2:j]
                if not stack or stack.pop() != tag:
                    return False
                i = j + 1
            elif code.startswith("<", i):
                j = code.find(">", i)
                if j == -1:
                    return False
                tag = code[i+1:j]
                # Check length, ensure it only contains uppercase alphabetic characters
                if not (1 <= len(tag) <= 9 and tag.isalpha() and tag.isupper()):
                    return False
                stack.append(tag)
                i = j + 1
            else:
                i += 1
                
        return not stack