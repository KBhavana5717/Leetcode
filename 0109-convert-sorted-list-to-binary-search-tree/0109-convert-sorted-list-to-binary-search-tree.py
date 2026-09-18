class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        # Step 1: Convert linked list values into a Python list
        nums = []
        current = head
        while current:
            nums.append(current.val)
            current = current.next
        
        # Step 2: Recursively build a height-balanced BST from the list
        def helper(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
        
        return helper(0, len(nums) - 1)