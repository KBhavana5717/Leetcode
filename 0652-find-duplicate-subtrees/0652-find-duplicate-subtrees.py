from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = defaultdict(int)
        result = []
        
        def serialize(node):
            if not node:
                return "#"
            
            # Serialize current subtree as a tuple/string format
            serial = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            
            count[serial] += 1
            # Add to result exactly once when we hit the second occurrence
            if count[serial] == 2:
                result.append(node)
                
            return serial
            
        serialize(root)
        return result