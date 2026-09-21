"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        
        def helper(r: int, c: int, length: int) -> 'Node':
            # Check if all elements in the current sub-grid are the same
            all_same = True
            first_val = grid[r][c]
            
            for i in range(r, r + length):
                for j in range(c, c + length):
                    if grid[i][j] != first_val:
                        all_same = False
                        break
                if not all_same:
                    break
                    
            # If all values are the same, return a leaf node
            if all_same:
                return Node(val=bool(first_val), isLeaf=True)
            
            # Otherwise, divide into 4 sub-grids and create an internal node
            half = length // 2
            top_left = helper(r, c, half)
            top_right = helper(r, c + half, half)
            bottom_left = helper(r + half, c, half)
            bottom_right = helper(r + half, c + half, half)
            
            return Node(
                val=True, # Value can be True or False when isLeaf is False
                isLeaf=False,
                topLeft=top_left,
                topRight=top_right,
                bottomLeft=bottom_left,
                bottomRight=bottom_right
            )

        return helper(0, 0, len(grid))