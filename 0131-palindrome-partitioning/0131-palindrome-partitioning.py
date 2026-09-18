class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        
        def dfs(start: int, path: list[str]):
            # If we've reached the end of the string, add the current path to results
            if start == len(s):
                result.append(path.copy())
                return
                
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                # Check if the current substring is a palindrome
                if sub == sub[::-1]:
                    path.append(sub)
                    dfs(end, path)
                    path.pop()  # Backtrack
                    
        dfs(0, [])
        return result