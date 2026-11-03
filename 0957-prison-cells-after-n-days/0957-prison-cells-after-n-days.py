class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        seen = {}
        while n > 0:
            state_tuple = tuple(cells)
            if state_tuple in seen:
                n %= (seen[state_tuple] - n)
            seen[state_tuple] = n
            
            if n > 0:
                n -= 1
                next_cells = [0] * 8
                for i in range(1, 7):
                    if cells[i - 1] == cells[i + 1]:
                        next_cells[i] = 1
                    else:
                        next_cells[i] = 0
                cells = next_cells
                
        return cells