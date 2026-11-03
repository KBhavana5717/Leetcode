class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        low, high = 0, len(tokens) - 1
        current_score = max_score = 0
        
        while low <= high:
            if power >= tokens[low]:
                power -= tokens[low]
                current_score += 1
                low += 1
                max_score = max(max_score, current_score)
            elif current_score > 0:
                power += tokens[high]
                current_score -= 1
                high -= 1
            else:
                break
                
        return max_score