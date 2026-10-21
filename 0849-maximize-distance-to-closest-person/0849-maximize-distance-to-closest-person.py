class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        n = len(seats)
        prev = -1          # index of the last occupied seat seen
        best = 0

        for i in range(n):
            if seats[i] == 1:
                if prev == -1:
                    best = i                      # empty seats at the left edge
                else:
                    best = max(best, (i - prev) // 2)   # between two people
                prev = i

        best = max(best, n - 1 - prev)            # empty seats at the right edge
        return best