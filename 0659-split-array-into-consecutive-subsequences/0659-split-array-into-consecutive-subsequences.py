from collections import Counter

class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        left = Counter(nums)
        tail = Counter()
        
        for x in nums:
            if left[x] == 0:
                continue
            
            # 1. Try to append to an existing subsequence ending at x - 1
            if tail[x - 1] > 0:
                tail[x - 1] -= 1
                tail[x] += 1
            # 2. Try to start a new subsequence of length 3: [x, x + 1, x + 2]
            elif left[x + 1] > 0 and left[x + 2] > 0:
                left[x + 1] -= 1
                left[x + 2] -= 1
                tail[x + 2] += 1
            # 3. If neither works, it's impossible
            else:
                return False
            
            left[x] -= 1
            
        return True