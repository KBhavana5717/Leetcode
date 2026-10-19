class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if start.replace('X', '') != result.replace('X', ''):
            return False
            
        p1, p2 = 0, 0
        n = len(start)
        
        while p1 < n and p2 < n:
            while p1 < n and start[p1] == 'X':
                p1 += 1
            while p2 < n and result[p2] == 'X':
                p2 += 1
                
            if p1 == n or p2 == n:
                break
                
            if start[p1] != result[p2]:
                return False
                
            if start[p1] == 'L' and p1 < p2:
                return False
            if start[p1] == 'R' and p1 > p2:
                return False
                
            p1 += 1
            p2 += 1
            
        return True