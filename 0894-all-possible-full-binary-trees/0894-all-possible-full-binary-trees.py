class Solution:
    def __init__(self):
        self.memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        if n in self.memo:
            return self.memo[n]
        
        res = []
        # i represents the number of nodes in the left subtree
        for i in range(1, n, 2):
            j = n - 1 - i  # nodes in the right subtree
            left_trees = self.allPossibleFBT(i)
            right_trees = self.allPossibleFBT(j)
            
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(0, left, right)
                    res.append(root)
                    
        self.memo[n] = res
        return res