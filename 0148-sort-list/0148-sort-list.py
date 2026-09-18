# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty or has only one node
        if not head or not head.next:
            return head
            
        # Step 1: Split the list into two halves using slow and fast pointers
        left = head
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        # Cut the list into two halves
        prev.next = None
        right = slow
        
        # Step 2: Recursively sort both halves
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)
        
        # Step 3: Merge the sorted halves
        return self.merge(left_sorted, right_sorted)
        
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        # Attach any remaining nodes
        curr.next = l1 if l1 else l2
        
        return dummy.next