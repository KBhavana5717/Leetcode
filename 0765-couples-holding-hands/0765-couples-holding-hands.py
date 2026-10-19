class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        ans = 0
        pos = {x: i for i, x in enumerate(row)}
        
        for i in range(0, len(row), 2):
            first = row[i]
            second = first ^ 1
            
            if row[i + 1] != second:
                ans += 1
                target_idx = pos[second]
                
                # Swap in row
                row[i + 1], row[target_idx] = row[target_idx], row[i + 1]
                
                # Update positions
                pos[row[target_idx]] = target_idx
                pos[row[i + 1]] = i + 1
                
        return ans