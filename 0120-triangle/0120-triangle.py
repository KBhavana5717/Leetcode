class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # Start from the row above the bottom-most row and move upwards
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Add the minimum of the two adjacent numbers from the row below
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
                
        # The top element now holds the minimum path sum
        return triangle[0][0]