class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        # Compute prefix sums
        prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
            
        def count_and_merge_sort(left: int, right: int) -> int:
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            count = count_and_merge_sort(left, mid) + count_and_merge_sort(mid + 1, right)
            
            # Count range sums crossing mid
            i = mid + 1
            j = mid + 1
            for left_idx in range(left, mid + 1):
                while i <= right and prefix_sums[i] - prefix_sums[left_idx] < lower:
                    i += 1
                while j <= right and prefix_sums[j] - prefix_sums[left_idx] <= upper:
                    j += 1
                count += (j - i)
                
            # Standard merge step
            sorted_subarray = []
            l, r = left, mid + 1
            while l <= mid and r <= right:
                if prefix_sums[l] <= prefix_sums[r]:
                    sorted_subarray.append(prefix_sums[l])
                    l += 1
                else:
                    sorted_subarray.append(prefix_sums[r])
                    r += 1
            while l <= mid:
                sorted_subarray.append(prefix_sums[l])
                l += 1
            while r <= right:
                sorted_subarray.append(prefix_sums[r])
                r += 1
                
            prefix_sums[left:right + 1] = sorted_subarray
            return count

        return count_and_merge_sort(0, len(prefix_sums) - 1)