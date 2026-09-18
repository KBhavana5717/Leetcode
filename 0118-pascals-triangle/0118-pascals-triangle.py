class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        
        for i in range(1, numRows):
            prev_row = result[-1]
            current_row = [1] # Every row starts with 1
            
            # Calculate intermediate values using the previous row
            for j in range(1, len(prev_row)):
                current_row.append(prev_row[j - 1] + prev_row[j])
                
            current_row.append(1) # Every row ends with 1
            result.append(current_row)
            
        return result