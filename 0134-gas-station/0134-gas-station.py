class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # If total gas is less than total cost, completion is impossible
        if sum(gas) < sum(cost):
            return -1
            
        total_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            
            # If tank goes negative, we cannot start from start_index up to i
            if total_tank < 0:
                start_index = i + 1
                total_tank = 0
                
        return start_index