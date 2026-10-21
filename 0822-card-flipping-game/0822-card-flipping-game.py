class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        same = {f for f, b in zip(fronts, backs) if f == b}
        
        ans = 99999
        for x in fronts + backs:
            if x not in same:
                if x < ans:
                    ans = x
                    
        return ans if ans != 99999 else 0