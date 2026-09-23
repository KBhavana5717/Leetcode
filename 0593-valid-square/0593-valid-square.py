class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(pA, pB):
            return (pA[0] - pB[0]) ** 2 + (pA[1] - pB[1]) ** 2
        
        points = [p1, p2, p3, p4]
        dists = []
        
        # Calculate distances between all unique pairs of points
        for i in range(4):
            for j in range(i + 1, 4):
                dists.append(dist(points[i], points[j]))
                
        dists.sort()
        
        # A valid square must have:
        # 1. Four equal sides (the 4 smallest distances)
        # 2. Two equal diagonals (the 2 largest distances)
        # 3. Distance > 0 (all points must be unique)
        return (dists[0] > 0 and 
                dists[0] == dists[1] == dists[2] == dists[3] and 
                dists[4] == dists[5])