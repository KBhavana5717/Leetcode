class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        # Sort the pairs based on their ending elements
        pairs.sort(key=lambda x: x[1])
        
        current_end = float('-inf')
        chain_length = 0
        
        for pair in pairs:
            # If the start of the current pair is greater than the end of the previous chain element
            if pair[0] > current_end:
                current_end = pair[1]
                chain_length += 1
                
        return chain_length