import random

class Solution:

    def __init__(self, nums: list[int]):
        self.original = list(nums)
        self.array = nums

    def reset(self) -> list[int]:
        # Restore the array to its original configuration
        self.array = list(self.original)
        return self.array

    def shuffle(self) -> list[int]:
        # Create a copy to shuffle, or shuffle the working array directly
        ans = list(self.array)
        n = len(ans)
        
        # Fisher-Yates Shuffle algorithm
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            ans[i], ans[j] = ans[j], ans[i]
            
        return ans