class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Find the intersection of both arrays using sets
        return list(set(nums1) & set(nums2))