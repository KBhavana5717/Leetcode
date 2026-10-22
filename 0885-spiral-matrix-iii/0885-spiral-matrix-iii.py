class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        res = [[rStart, cStart]]
        r, c = rStart, cStart
        steps = 1
        dr, dc = 0, 1  # Initially facing East
        
        while len(res) < rows * cols:
            for _ in range(2):
                for _ in range(steps):
                    r, c = r + dr, c + dc
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                # Turn clockwise: East -> South -> West -> North -> East
                dr, dc = dc, -dr
            steps += 1
            
        return res