class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        if not matrix or not matrix[0]:
            return res
            
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 1. Traverse from left to right along the top row
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            
            # 2. Traverse from top to bottom down the right column
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1
            
            if top <= bottom:
                # 3. Traverse from right to left along the bottom row
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
                
            if left <= right:
                # 4. Traverse from bottom to top up the left column
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1
                
        return res