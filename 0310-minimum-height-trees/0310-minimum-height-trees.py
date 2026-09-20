from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        # Base case for a single node graph
        if n == 1:
            return [0]
        
        # Build adjacency list and degree count for each node
        adj = {i: set() for i in range(n)}
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            
        # Initialize queue with all leaf nodes (degree == 1)
        leaves = deque([i for i in range(n) if len(adj[i]) == 1])
        
        # Trim leaves until 2 or fewer nodes remain (the centroid(s))
        remaining_nodes = n
        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count
            
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                # Remove the leaf from its neighbor's adjacency set
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                
                # If neighbor becomes a leaf, add it to the queue
                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)
                    
        return list(leaves)