class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[n - 1][n - 1]
        
        def countLessOrEqual(mid):
            count = 0
            row, col = n - 1, 0  # Start from bottom-left corner
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += (row + 1)  # All elements above in this column are also <= mid
                    col += 1
                else:
                    row -= 1
            return count

        while low < high:
            mid = (low + high) // 2
            if countLessOrEqual(mid) < k:
                low = mid + 1
            else:
                high = mid
                
        return low