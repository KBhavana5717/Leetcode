class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        lo, hi = 0, len(arr) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < arr[mid + 1]:
                lo = mid + 1      # uphill, peak is to the right
            else:
                hi = mid          # downhill, peak is here or to the left

        return lo