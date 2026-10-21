class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted((val, i) for i, val in enumerate(nums2))

        ans = [0] * len(nums1)
        left, right = 0, len(nums1) - 1

        for val, i in reversed(sorted_nums2):
            if sorted_nums1[right] > val:
                ans[i] = sorted_nums1[right]
                right -= 1
            else:
                ans[i] = sorted_nums1[left]
                left += 1

        return ans