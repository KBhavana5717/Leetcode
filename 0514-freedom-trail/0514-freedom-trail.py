from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)
        
        # Map each character to all its indices in the ring
        char_indices = defaultdict(list)
        for i, char in enumerate(ring):
            char_indices[char].append(i)
            
        # DP state: memoization dictionary or table
        # To compute key step by step, we can use a dictionary mapping ring index -> min steps
        # Initially, at step 0, ring index 0 has 0 cost.
        dp = {0: 0}
        
        for char in key:
            next_dp = defaultdict(lambda: float('inf'))
            for curr_ring_idx, steps in dp.items():
                for target_ring_idx in char_indices[char]:
                    # Calculate clockwise and anticlockwise distance
                    dist = abs(curr_ring_idx - target_ring_idx)
                    clockwise_dist = min(dist, n - dist)
                    
                    # Total steps = current steps + rotation steps + button press (1 step)
                    total_steps = steps + clockwise_dist + 1
                    
                    if total_steps < next_dp[target_ring_idx]:
                        next_dp[target_ring_idx] = total_steps
            dp = next_dp
            
        return min(dp.values())