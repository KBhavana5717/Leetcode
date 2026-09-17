class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        
        while top <= bottom and left <= right:
            # 1. Fill from left to right along the top row
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1
            
            # 2. Fill from top to bottom down the right column
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1
            
            # 3. Fill from right to left along the bottom row
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
            
            # 4. Fill from bottom to top up the left column
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
            
        return matrix