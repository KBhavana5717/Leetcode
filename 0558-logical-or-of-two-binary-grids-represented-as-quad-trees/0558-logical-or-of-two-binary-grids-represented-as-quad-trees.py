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
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # Case 1: If quadTree1 is a leaf node
        if quadTree1.isLeaf:
            # If its value is True (all 1s), logical OR with anything is True (1)
            if quadTree1.val:
                return Node(True, True, None, None, None, None)
            # If its value is False (all 0s), logical OR results in quadTree2
            else:
                return quadTree2
                
        # Case 2: If quadTree2 is a leaf node
        if quadTree2.isLeaf:
            if quadTree2.val:
                return Node(True, True, None, None, None, None)
            else:
                return quadTree1
                
        # Case 3: Neither is a leaf, so we recurse on all 4 corresponding children
        top_left = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        top_right = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottom_left = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottom_right = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        
        # Optimization: If all 4 children are leaves and have the same value and leaf status, 
        # we merge them into a single leaf node.
        if (top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and
            top_left.val == top_right.val == bottom_left.val == bottom_right.val):
            return Node(top_left.val, True, None, None, None, None)
            
        # Otherwise, return an internal node with the four child nodes
        return Node(False, False, top_left, top_right, bottom_left, bottom_right)