from collections import deque

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        start_state = "".join(str(board[r][c]) for r in range(2) for c in range(3))
        target_state = "123450"
        
        # Adjacency list for indices 0 to 5 on a 2x3 board
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        queue = deque([(start_state, start_state.index('0'), 0)])
        visited = {start_state}
        
        while queue:
            state, zero_idx, moves = queue.popleft()
            
            if state == target_state:
                return moves
                
            state_list = list(state)
            for neighbor in neighbors[zero_idx]:
                # Swap '0' with the neighbor
                state_list[zero_idx], state_list[neighbor] = state_list[neighbor], state_list[zero_idx]
                next_state = "".join(state_list)
                
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, neighbor, moves + 1))
                
                # Swap back for the next iteration
                state_list[zero_idx], state_list[neighbor] = state_list[neighbor], state_list[zero_idx]
                
        return -1