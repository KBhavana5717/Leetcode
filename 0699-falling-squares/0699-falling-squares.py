class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        heights = []  # stores (left, right, height) for each square that has landed
        ans = []
        max_height = 0

        for left, side in positions:
            right = left + side
            # Base height starts at 0 (ground)
            base_height = 0
            
            # Check overlap with all previously landed squares
            for prev_left, prev_right, prev_height in heights:
                # Check if the intervals overlap
                if not (right <= prev_left or left >= prev_right):
                    base_height = max(base_height, prev_height)
            
            curr_height = base_height + side
            heights.append((left, right, curr_height))
            
            max_height = max(max_height, curr_height)
            ans.append(max_height)

        return ans