from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        queue = deque([(startGene, 0)])
        choices = ['A', 'C', 'G', 'T']
        
        while queue:
            curr_gene, steps = queue.popleft()
            
            if curr_gene == endGene:
                return steps
            
            # Try all possible single-character mutations
            for i in range(len(curr_gene)):
                for char in choices:
                    if char == curr_gene[i]:
                        continue
                    
                    mutation = curr_gene[:i] + char + curr_gene[i+1:]
                    
                    if mutation in bank_set:
                        bank_set.remove(mutation) # Mark as visited by removing from bank
                        queue.append((mutation, steps + 1))
                        
        return -1