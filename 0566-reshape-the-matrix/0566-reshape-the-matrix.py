class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        # If the total number of elements doesn't match, reshaping is illegal
        if m * n != r * c:
            return mat
        
        # Flatten the original matrix and reshape it into r rows of c elements
        flat = [num for row in mat for num in row]
        return [flat[i * c:(i + 1) * c] for i in range(r)]