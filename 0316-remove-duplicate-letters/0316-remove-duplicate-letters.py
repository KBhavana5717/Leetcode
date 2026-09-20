class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Find the last occurrence index of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        visited = set()
        
        for i, char in enumerate(s):
            if char in visited:
                continue
                
            # Pop characters from stack if they are greater than the current character
            # and they appear again later in the string
            while stack and stack[-1] > char and i < last_occurrence[stack[-1]]:
                visited.remove(stack.pop())
                
            stack.append(char)
            visited.add(char)
            
        return "".join(stack)