import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []
            
        min_heap = []
        # Push the first min(k, len(nums1)) elements paired with nums2[0]
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
            
        result = []
        
        while min_heap and len(result) < k:
            current_sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            # If there is a next element in nums2 for the current nums1[i], push it to the heap
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                
        return result