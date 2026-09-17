class Solution:
    def isValid(self, s):
        stack=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            elif i==')' or i==']' or i=='}':
                if not stack:
                    return False
                open_bracket=stack.pop()
                if not self.is_matching_pair(open_bracket,i):
                    return False
        if not stack:
            return True
        else:
            return False
    def is_matching_pair(self,open_bracket,close_bracket):
        return (open_bracket=='(' and close_bracket==')') or \
           (open_bracket=='{' and close_bracket=='}') or \
           (open_bracket=='[' and close_bracket==']')
                                      


        
        