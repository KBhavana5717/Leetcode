class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)
        
        for i in range(n):
            if nums[i] == 0:
                continue
                
            # Simulate the path starting from index i
            curr = i
            nit_is_forward = nums[i] > 0
            
            # Use a unique marker for the current traversal (e.g., current index + 10000, 
            # or we can use a local set, but modifying numbers or using a visited state is faster. 
            # Here, let's use a distinct value or simply step through with a local tracking approach.)
            
            # To stay strictly O(1) space, we can mark visited nodes by modifying them 
            # with a value outside the valid range, or use slow/fast pointers.
            # Let's use the slow and fast pointer (Floyd's Cycle-Finding Algorithm) adapted for this:
            
            slow = i
            fast = i
            
            # Helper to calculate next index
            def get_next(current_idx):
                return (current_idx + nums[current_idx]) % n

            while True:
                next_slow = get_next(slow)
                # Check direction or self-loop for slow
                if (nums[slow] > 0) != nit_is_forward or (nums[next_slow] > 0) != nit_is_forward or next_slow == slow:
                    break
                    
                next_fast = get_next(fast)
                if (nums[fast] > 0) != nit_is_forward or (nums[next_fast] > 0) != nit_is_forward or next_fast == fast:
                    break
                    
                next_fast_2 = get_next(next_fast)
                if (nums[next_fast] > 0) != nit_is_forward or (nums[next_fast_2] > 0) != nit_is_forward or next_fast_2 == next_fast:
                    break
                    
                slow = next_slow
                fast = next_fast_2
                
                if slow == fast:
                    return True
                    
            # Mark all nodes in this invalid path as 0 so we don't re-explore them
            curr = i
            while nums[curr] != 0 and (nums[curr] > 0) == nit_is_forward:
                next_node = get_next(curr)
                nums[curr] = 0
                curr = next_node
                
        return False