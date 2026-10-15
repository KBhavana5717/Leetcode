import random

class Solution:

    def __init__(self, n: int, blacklist: list[int]):
        self.m = n - len(blacklist)
        self.mapping = {}
        
        black_set = set()
        for b in blacklist:
            if b >= self.m:
                black_set.add(b)
        
        curr = self.m
        for b in blacklist:
            if b < self.m:
                while curr in black_set:
                    curr += 1
                self.mapping[b] = curr
                curr += 1

    def pick(self) -> int:
        val = random.randint(0, self.m - 1)
        return self.mapping.get(val, val)