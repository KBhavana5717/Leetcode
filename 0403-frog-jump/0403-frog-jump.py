class Solution:
    def canCross(self, stones: list[int]) -> bool:
        from collections import defaultdict
        
        # Map each stone position to a set of jump sizes that can reach it
        stone_positions = set(stones)
        jump_map = defaultdict(set)
        jump_map[0].add(0)
        
        for stone in stones:
            for k in jump_map[stone]:
                for next_jump in (k - 1, k, k + 1):
                    if next_jump > 0 and (stone + next_jump) in stone_positions:
                        jump_map[stone + next_jump].add(next_jump)
                        
        # If the last stone has any valid jumps leading to it, return True
        return len(jump_map[stones[-1]]) > 0