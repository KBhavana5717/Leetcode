from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Count frequencies of elements in nums1
        counts = Counter(nums1)
        result = []
        
        # Check elements in nums2 against the counter
        for num in nums2:
            if num in counts and counts[num] > 0:
                result.append(num)
                counts[num] -= 1
                
        return result