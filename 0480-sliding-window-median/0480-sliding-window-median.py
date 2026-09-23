import heapq
from collections import defaultdict
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # small: max-heap (stored as negatives) holds the smaller half
        # large: min-heap holds the larger half
        small, large = [], []
        delayed = defaultdict(int)   # value -> count of pending removals
        small_size, large_size = 0, 0  # "true" sizes, excluding delayed removals

        def prune(heap, is_small):
            # Remove values from the top of the heap that are marked for lazy deletion
            while heap:
                top = -heap[0] if is_small else heap[0]
                if delayed[top] > 0:
                    delayed[top] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def rebalance():
            nonlocal small_size, large_size
            if small_size > large_size + 1:
                val = -heapq.heappop(small)
                small_size -= 1
                heapq.heappush(large, val)
                large_size += 1
                prune(small, True)
            elif small_size < large_size:
                val = heapq.heappop(large)
                large_size -= 1
                heapq.heappush(small, -val)
                small_size += 1
                prune(large, False)

        def add(num):
            nonlocal small_size, large_size
            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1
            rebalance()

        def remove(num):
            nonlocal small_size, large_size
            delayed[num] += 1
            if small and num <= -small[0]:
                small_size -= 1
                if num == -small[0]:
                    prune(small, True)
            else:
                large_size -= 1
                if large and num == large[0]:
                    prune(large, False)
            rebalance()

        def get_median():
            if k % 2 == 1:
                return float(-small[0])
            return (-small[0] + large[0]) / 2.0

        result = []
        for i in range(len(nums)):
            add(nums[i])
            if i >= k - 1:
                result.append(get_median())
                remove(nums[i - k + 1])

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # Expected: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    print(sol.medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], 3))
    # Expected: [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]