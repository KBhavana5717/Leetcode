class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        result = [0] * n
        indices = list(range(n))  # Track original indices

        def merge_sort(left, right):
            if right - left <= 1:
                return

            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid, right)

            temp = []
            i, j = left, mid
            right_count = 0

            while i < mid and j < right:
                if nums[indices[j]] < nums[indices[i]]:
                    temp.append(indices[j])
                    right_count += 1
                    j += 1
                else:
                    temp.append(indices[i])
                    result[indices[i]] += right_count
                    i += 1

            while i < mid:
                temp.append(indices[i])
                result[indices[i]] += right_count
                i += 1

            while j < right:
                temp.append(indices[j])
                j += 1

            indices[left:right] = temp

        merge_sort(0, n)
        return result
