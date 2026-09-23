class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross_product(p, q, r):
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])
        
        if len(trees) <= 3:
            return trees
            
        # Sort the points lexicographically (by x, then by y)
        trees.sort()
        
        # Build the lower hull
        lower = []
        for p in trees:
            while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)
            
        # Build the upper hull
        upper = []
        for p in reversed(trees):
            while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)
            
        # Combine both hulls and remove duplicate points using a set
        return list(map(list, set(tuple(p) for p in lower + upper)))