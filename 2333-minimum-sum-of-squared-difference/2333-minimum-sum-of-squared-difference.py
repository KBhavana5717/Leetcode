class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Calculate absolute differences for each pair
        d = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        
        # If total operations are enough to reduce all differences to 0
        if sum(d) <= k:
            return 0
        
        # Binary search for the optimal maximum difference threshold
        left, right = 0, max(d)
        while left < right:
            mid = (left + right) >> 1
            # Check if we can reduce all differences > mid to mid using <= k operations
            if sum(max(v - mid, 0) for v in d) <= k:
                right = mid
            else:
                left = mid + 1
        
        # Apply reductions down to 'left' threshold
        for i in range(len(d)):
            if d[i] > left:
                k -= (d[i] - left)
                d[i] = left
                
        # Distribute any remaining operations (k) to elements equal to 'left'
        for i in range(len(d)):
            if k > 0 and d[i] == left:
                d[i] -= 1
                k -= 1
                
        # Calculate the final minimum sum of squared differences
        return sum(v * v for v in d)