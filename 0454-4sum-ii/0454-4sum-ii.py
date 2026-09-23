from collections import Counter

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        # Step 1: Count frequencies of all possible sums from nums1 and nums2
        sum_count = Counter(u + v for u in nums1 for v in nums2)
        
        # Step 2: Count how many times the complement (-(u + v)) appears in sum_count
        count = 0
        for u in nums3:
            for v in nums4:
                complement = -(u + v)
                if complement in sum_count:
                    count += sum_count[complement]
                    
        return count