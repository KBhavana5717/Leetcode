class Solution:
    def containVirus(self, isInfected: list[list[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        total_walls = 0
        
        while True:
            visited = set()
            regions = []
            
            # Step 1: Identify all connected viral regions
            for r in range(m):
                for c in range(n):
                    if isInfected[r][c] == 1 and (r, c) not in visited:
                        q = [(r, c)]
                        visited.add((r, c))
                        region = {(r, c)}
                        threatened = set()
                        walls = 0
                        
                        idx = 0
                        while idx < len(q):
                            curr_r, curr_c = q[idx]
                            idx += 1
                            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nr, nc = curr_r + dr, curr_c + dc
                                if 0 <= nr < m and 0 <= nc < n:
                                    if isInfected[nr][nc] == 1 and (nr, nc) not in visited:
                                        visited.add((nr, nc))
                                        region.add((nr, nc))
                                        q.append((nr, nc))
                                    elif isInfected[nr][nc] == 0:
                                        threatened.add((nr, nc))
                                        walls += 1
                                        
                        regions.append((region, threatened, walls))
                        
            if not regions:
                break
                
            # Find the region that threatens the most uninfected cells
            max_threat_idx = 0
            for i in range(1, len(regions)):
                if len(regions[i][1]) > len(regions[max_threat_idx][1]):
                    max_threat_idx = i
                    
            # Quarantine the most threatening region
            walls_built = 0
            for i, (region, threatened, walls) in enumerate(regions):
                if i == max_threat_idx:
                    total_walls += walls
                    for r, c in region:
                        isInfected[r][c] = -1  # Mark as contained
                else:
                    # Let this region spread
                    for r, c in region:
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and isInfected[nr][nc] == 0:
                                isInfected[nr][nc] = 1
                                
            # If all viral regions are contained or fully spread, we can stop
            # Check if any region can still spread
            can_spread = False
            for r in range(m):
                for c in range(n):
                    if isInfected[r][c] == 1:
                        can_spread = True
            if not can_spread:
                break
                
        return total_walls