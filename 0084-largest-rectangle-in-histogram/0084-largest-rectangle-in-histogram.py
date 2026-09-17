class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)
        
        for i in range(n + 1):
            # Use 0 as a sentinel value for the end of the array
            current_height = heights[i] if i < n else 0
            
            while stack and current_height < heights[stack[-1]]:
                height = heights[stack.pop()]
                # Width calculation: current index 'i' is the right boundary, 
                # and the new stack top is the left boundary.
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
                
            stack.append(i)
            
        return max_area