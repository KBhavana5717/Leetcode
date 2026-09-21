import random
from collections import defaultdict

class Solution:

    def __init__(self, nums: list[int]):
        # Map each number to a list of its indices
        self.indices_map = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices_map[num].append(i)

    def pick(self, target: int) -> int:
        # Randomly choose one index from the list of indices for the target
        return random.choice(self.indices_map[target])