from collections import Counter
import math

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        count = Counter(answers)
        res = 0
        for x, freq in count.items():
            group_size = x + 1
            num_groups = math.ceil(freq / group_size)
            res += num_groups * group_size
        return res