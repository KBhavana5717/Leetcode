class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_path, open_count, close_count):
            # If the current string has reached a length of 2 * n, it's a valid combination
            if len(current_path) == 2 * n:
                result.append("".join(current_path))
                return
                
            # We can add an opening parenthesis if we haven't used all n open brackets
            if open_count < n:
                current_path.append('(')
                backtrack(current_path, open_count + 1, close_count)
                current_path.pop()
                
            # We can add a closing parenthesis if there are unclosed open brackets
            if close_count < open_count:
                current_path.append(')')
                backtrack(current_path, open_count, close_count + 1)
                current_path.pop()
                
        backtrack([], 0, 0)
        return result