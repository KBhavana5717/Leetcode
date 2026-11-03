class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        i = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return len(stack) == 0