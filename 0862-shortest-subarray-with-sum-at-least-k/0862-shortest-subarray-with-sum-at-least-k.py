from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()          # indices with increasing prefix values
        best = n + 1

        for i in range(n + 1):
            # shrink from the front: the oldest index gives a valid subarray
            while dq and prefix[i] - prefix[dq[0]] >= k:
                best = min(best, i - dq.popleft())

            # keep the deque increasing: a larger old prefix is never useful
            while dq and prefix[dq[-1]] >= prefix[i]:
                dq.pop()

            dq.append(i)

        return best if best <= n else -1