class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_count = {}
        guess_count = {}
        
        for s_char, g_char in zip(secret, guess):
            if s_char == g_char:
                bulls += 1
            else:
                secret_count[s_char] = secret_count.get(s_char, 0) + 1
                guess_count[g_char] = guess_count.get(g_char, 0) + 1
                
        # Count cows by taking the minimum overlap of unmatched digits
        for char in guess_count:
            if char in secret_count:
                cows += min(secret_count[char], guess_count[char])
                
        return f"{bulls}A{cows}B"