class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        # Step 1: Sort both greed factors and cookie sizes
        g.sort()
        s.sort()
        
        child_ptr = 0
        cookie_ptr = 0
        
        # Step 2: Iterate through both lists using two pointers
        while child_ptr < len(g) and cookie_ptr < len(s):
            # If the current cookie satisfies the current child's greed
            if s[cookie_ptr] >= g[child_ptr]:
                child_ptr += 1  # Move to the next child
            
            # Always move to the next cookie, whether used or too small
            cookie_ptr += 1
            
        # The number of content children is equal to the child pointer index
        return child_ptr