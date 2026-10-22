class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        obs_set = set(tuple(obs) for obs in obstacles)
        
        # Directions: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0  # Starts facing North
        x, y = 0, 0
        max_dist = 0
        
        for cmd in commands:
            if cmd == -2:  # Turn left 90 degrees
                curr_dir = (curr_dir - 1) % 4
            elif cmd == -1:  # Turn right 90 degrees
                curr_dir = (curr_dir + 1) % 4
            else:  # Move forward k units
                dx, dy = directions[curr_dir]
                for _ in range(cmd):
                    next_x, next_y = x + dx, y + dy
                    if (next_x, next_y) in obs_set:
                        break
                    x, y = next_x, next_y
                    max_dist = max(max_dist, x * x + y * y)
                    
        return max_dist