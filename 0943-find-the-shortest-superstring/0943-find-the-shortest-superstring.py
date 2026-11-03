class Solution:
    def shortestSuperstring(self, words: list[str]) -> str:
        n = len(words)
        
        # Precalculate overlap lengths between every pair of words
        # overlap[i][j] is the length of the suffix of words[i] that matches the prefix of words[j]
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for k in range(min(len(words[i]), len(words[j])), 0, -1):
                    if words[i].endswith(words[j][:k]):
                        overlap[i][j] = k
                        break
                        
        # dp[mask][i] stores the shortest superstring formed by visiting a subset of words represented by `mask`, ending with words[i]
        dp = [[""] * n for _ in range(1 << n)]
        
        for i in range(n):
            dp[1 << i][i] = words[i]
            
        for mask in range(1 << n):
            for i in range(n):
                if not (mask & (1 << i)):
                    continue
                if not dp[mask][i]:
                    continue
                for j in range(n):
                    if mask & (1 << j):
                        continue
                    next_mask = mask | (1 << j)
                    candidate = dp[mask][i] + words[j][overlap[i][j]:]
                    if not dp[next_mask][j] or len(candidate) < len(dp[next_mask][j]):
                        dp[next_mask][j] = candidate
                        
        full_mask = (1 << n) - 1
        return min(dp[full_mask], key=len)