class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        ple = [-1] * n  # Previous Less Element index
        nle = [n] * n  # Next Less or Equal Element index
        
        stack = []
        # Find Previous Less Element (strictly less '>' to handle duplicates)
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                ple[i] = stack[-1]
            stack.append(i)
            
        stack = []
        # Find Next Less or Equal Element (non-strict '>=' from right to left)
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                nle[i] = stack[-1]
            stack.append(i)
            
        # Calculate the total sum of contributions
        total_sum = 0
        for i in range(n):
            left_count = i - ple[i]
            right_count = nle[i] - i
            total_sum = (total_sum + arr[i] * left_count * right_count) % MOD
            
        return total_sum