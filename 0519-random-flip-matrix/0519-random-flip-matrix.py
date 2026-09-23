import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}
        self.reset()

    def flip(self) -> list[int]:
        # Pick a random index from 0 to self.total - 1
        r = random.randint(0, self.total - 1)
        
        # If this index has been mapped, use the mapped value; otherwise use r itself
        idx = self.map.get(r, r)
        
        # Decrease total available choices
        self.total -= 1
        
        # Map the current random index to the last available element in the range
        self.map[r] = self.map.get(self.total, self.total)
        
        # Convert 1D index back to 2D (row, col)
        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        # Re-initialize variables safely using self.m and self.n
        self.total = self.m * self.n
        self.map.clear()