class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # Start with the 0th row [1]
        row = [1] * (rowIndex + 1)
        
        for i in range(1, rowIndex + 1):
            # Update values backwards from right to left
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
                
        return row