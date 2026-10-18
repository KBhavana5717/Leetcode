class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        visited = set()
        ans = []
        
        def dfs(node):
            for x in map(str, range(k - 1, -1, -1)):
                nxt = node + x
                if nxt not in visited:
                    visited.add(nxt)
                    dfs(nxt[1:])
                    ans.append(x)
                    
        dfs("0" * (n - 1))
        return "".join(ans) + "0" * (n - 1)