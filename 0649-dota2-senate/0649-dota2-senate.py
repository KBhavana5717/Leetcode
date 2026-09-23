from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()
        
        # Populate the queues with the indices of each party's senators
        for i, char in enumerate(senate):
            if char == 'R':
                radiant.append(i)
            else:
                dire.append(i)
                
        # Simulate the voting process
        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()
            
            # The senator with the smaller index acts first and bans the other
            if r_index < d_index:
                # Radiant senator bans Dire senator, Radiant survives to the next round
                radiant.append(r_index + n)
            else:
                # Dire senator bans Radiant senator, Dire survives to the next round
                dire.append(d_index + n)
                
        return "Radiant" if radiant else "Dire"