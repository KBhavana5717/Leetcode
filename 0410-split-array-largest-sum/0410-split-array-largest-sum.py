class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def can_split(target_sum: int) -> bool:
            subarrays = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > target_sum:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
            return True

        # The minimum possible max-sum is the maximum single element in nums
        # The maximum possible max-sum is the sum of all elements in nums
        left = max(nums)
        right = sum(nums)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if can_split(mid):
                ans = mid
                right = mid - 1  # Try to find a smaller valid maximum sum
            else:
                left = mid + 1   # Increase the allowed sum since mid is too small

        return ans