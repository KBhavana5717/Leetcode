class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Step 1: Map each node to its parent
        parent_map = {}
        def get_parents(node, parent=None):
            if not node:
                return
            if parent:
                parent_map[node] = parent
            get_parents(node.left, node)
            get_parents(node.right, node)
        
        get_parents(root)
        
        # Step 2: BFS to find all nodes at distance k
        queue = collections.deque([target])
        visited = {target}
        current_distance = 0
        
        while queue:
            if current_distance == k:
                return [node.val for node in queue]
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                # Check left child
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                
                # Check right child
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                
                # Check parent
                if node in parent_map and parent_map[node] not in visited:
                    visited.add(parent_map[node])
                    queue.append(parent_map[node])
            
            current_distance += 1
            
        return []