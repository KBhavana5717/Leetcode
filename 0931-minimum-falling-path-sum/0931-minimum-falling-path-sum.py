class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        
        # Start from the second row down to the last row
        for i in range(1, n):
            for j in range(n):
                # Get the minimum from the valid choices in the row above
                left_diagonal = matrix[i - 1][j - 1] if j > 0 else float('inf')
                directly_above = matrix[i - 1][j]
                right_diagonal = matrix[i - 1][j + 1] if j < n - 1 else float('inf')
                
                matrix[i][j] += min(left_diagonal, directly_above, right_diagonal)
                
        # The result is the minimum value in the last row
        return min(matrix[-1])