import random
import bisect

class Solution:

    def __init__(self, w: list[int]):
        self.prefix_sums = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sums.append(current_sum)
        self.total_sum = current_sum

    def pickIndex(self) -> int:
        # Generate a random target value between 1 and the total sum
        target = random.randint(1, self.total_sum)
        
        # Use binary search to find the corresponding index
        return bisect.bisect_left(self.prefix_sums, target)