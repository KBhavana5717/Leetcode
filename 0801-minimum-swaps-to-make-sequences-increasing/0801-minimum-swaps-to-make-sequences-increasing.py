class Solution:
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        not_swap = 0
        swap = 1
        
        for i in range(1, n):
            next_not_swap = float('inf')
            next_swap = float('inf')
            
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                next_not_swap = min(next_not_swap, not_swap)
                next_swap = min(next_swap, swap + 1)
                
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                next_not_swap = min(next_not_swap, swap)
                next_swap = min(next_swap, not_swap + 1)
                
            not_swap = next_not_swap
            swap = next_swap
            
        return min(not_swap, swap)