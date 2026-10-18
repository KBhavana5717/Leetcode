from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        allowed_map = defaultdict(list)
        for pattern in allowed:
            allowed_map[(pattern[0], pattern[1])].append(pattern[2])
            
        memo = {}
        
        def helper(row):
            if len(row) == 1:
                return True
            if row in memo:
                return memo[row]
                
            def get_next_rows(idx, current_built):
                if idx == len(row) - 1:
                    return helper(current_built)
                
                left, right = row[idx], row[idx + 1]
                if (left, right) not in allowed_map:
                    return False
                
                for top_block in allowed_map[(left, right)]:
                    if get_next_rows(idx + 1, current_built + top_block):
                        return True
                return False
                
            res = get_next_rows(0, "")
            memo[row] = res
            return res

        return helper(bottom)