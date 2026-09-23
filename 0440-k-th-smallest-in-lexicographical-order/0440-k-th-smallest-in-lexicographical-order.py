class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        # Helper function to calculate the number of steps/nodes between 
        # curr and curr + 1 within the limit n
        def count_steps(curr, n):
            steps = 0
            first = curr
            last = curr
            while first <= n:
                steps += min(n + 1, last + 1) - first
                first *= 10
                last = last * 10 + 9
            return steps

        curr = 1
        k -= 1  # 0-indexed count relative to the current position
        
        while k > 0:
            steps = count_steps(curr, n)
            if k >= steps:
                # If k is greater than or equal to the steps in the current subtree,
                # skip this entire subtree and move to the next sibling
                k -= steps
                curr += 1
            else:
                # If k is within the current subtree, go down to the first child
                curr *= 10
                k -= 1
                
        return curr