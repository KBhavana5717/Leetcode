class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res = []
        
        def backtrack(index, path):
            if index == len(s):
                res.append("".join(path))
                return
            
            if s[index].isalpha():
                path.append(s[index].lower())
                backtrack(index + 1, path)
                path.pop()
                
                path.append(s[index].upper())
                backtrack(index + 1, path)
                path.pop()
            else:
                path.append(s[index])
                backtrack(index + 1, path)
                path.pop()
                
        backtrack(0, [])
        return res