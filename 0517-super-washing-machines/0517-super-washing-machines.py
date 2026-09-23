class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        total_dresses = sum(machines)
        n = len(machines)
        
        # If total dresses cannot be evenly divided among all machines, it's impossible
        if total_dresses % n != 0:
            return -1
            
        target = total_dresses // n
        ans = 0
        current_balance = 0
        
        for dresses in machines:
            # Difference between current machine's dresses and target
            diff = dresses - target
            current_balance += diff
            
            # The maximum moves needed will be:
            # 1. The maximum dresses flowing through a single machine (absolute cumulative balance).
            # 2. The maximum dresses a single machine needs to send out (diff if positive).
            ans = max(ans, abs(current_balance), diff)
            
        return ans