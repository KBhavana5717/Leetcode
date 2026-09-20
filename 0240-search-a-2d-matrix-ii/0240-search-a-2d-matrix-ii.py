class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols - 1
        
        while r < rows and c >= 0:
            current = matrix[r][c]
            if current == target:
                return True
            elif current > target:
                c -= 1
            else:
                r += 1
                
        return False