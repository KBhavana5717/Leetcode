class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        next_greater = {}
        
        # Find the next greater element for each number in nums2 using a monotonic stack
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
            
        # Build the result for nums1 using the precomputed dictionary
        return [next_greater.get(num, -1) for num in nums1]