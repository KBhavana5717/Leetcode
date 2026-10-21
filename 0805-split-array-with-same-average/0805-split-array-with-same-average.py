class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        n = len(nums)
        if n == 1:
            return False
            
        # Shift all elements by multiplying by n to work with integers
        # sum(A) / k == total_sum / n  =>  sum(A) * n == total_sum * k
        A = [x * n - total_sum for x in nums]
        
        n1 = n // 2
        n2 = n - n1
        
        # Find all possible subset sums for the first half
        sums1 = [set() for _ in range(n1 + 1)]
        sums1[0].add(0)
        
        for x in A[:n1]:
            for i in range(n1 - 1, -1, -1):
                if sums1[i]:
                    for s in sums1[i]:
                        sums1[i + 1].add(s + x)
                        
        # Check if any subset in the first half has sum 0
        for i in range(1, n1 + 1):
            if 0 in sums1[i]:
                return True
                
        # Find all possible subset sums for the second half
        sums2 = [set() for _ in range(n2 + 1)]
        sums2[0].add(0)
        
        for x in A[n1:]:
            for i in range(n2 - 1, -1, -1):
                if sums2[i]:
                    for s in sums2[i]:
                        sums2[i + 1].add(s + x)
                        
        for i in range(1, n2 + 1):
            if 0 in sums2[i]:
                return True
                
        # Combine subsets from both halves
        all_sums1 = set()
        for i in range(1, n1 + 1):
            all_sums1.update(sums1[i])
            
        # Check if we can pick k elements total (some from first, some from second)
        # where the combined sum is 0, excluding picking all or none.
        for j in range(1, n2 + 1):
            for s2 in sums2[j]:
                if -s2 in all_sums1 and not (j == n2 and len(A) == n):
                    # Check individual sizes to ensure we don't pick 0 or all elements
                    for i in range(1, n1 + 1):
                        if s2 in {-s for s in sums1[i]}:
                            if not (i == n1 and j == n2):
                                return True
                                
        return False