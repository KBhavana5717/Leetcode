class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailingZeroes(n: int) -> int:
            count = 0
            while n > 0:
                count += n // 5
                n //= 5
            return count

        def binarySearch(target: int) -> int:
            left, right = 0, 5 * target + 1
            while left <= right:
                mid = (left + right) // 2
                if trailingZeroes(mid) < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        return binarySearch(k + 1) - binarySearch(k)