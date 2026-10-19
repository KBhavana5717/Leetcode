class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        def count(bound: int) -> int:
            res = 0
            curr = 0
            for x in nums:
                curr = curr + 1 if x <= bound else 0
                res += curr
            return res

        return count(right) - count(left - 1)