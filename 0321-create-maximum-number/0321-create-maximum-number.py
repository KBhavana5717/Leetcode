class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        
        # Helper to find the maximum subsequence of length 'length' from an array
        def getMaxSubsequence(nums, length):
            drop = len(nums) - length
            stack = []
            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:length]

        # Helper to merge two subsequences to form the largest number
        def merge(seq1, seq2):
            res = []
            s1, s2 = list(seq1), list(seq2)
            while s1 or s2:
                if s1 > s2:
                    res.append(s1.pop(0))
                else:
                    res.append(s2.pop(0))
            return res

        best = []
        m, n = len(nums1), len(nums2)
        
        # Iterate over all valid counts of digits to take from nums1
        for i in range(max(0, k - n), min(k, m) + 1):
            sub1 = getMaxSubsequence(nums1, i)
            sub2 = getMaxSubsequence(nums2, k - i)
            candidate = merge(sub1, sub2)
            if candidate > best:
                best = candidate
                
        return best