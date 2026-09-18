# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        
        curr = head.next
        head.next = None  # Start with a sorted list of length 1
        
        while curr:
            next_node = curr.next  # Save the next node to process
            
            # Find the correct position to insert 'curr' from the dummy node
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
                
            # Insert 'curr' between prev and prev.next
            curr.next = prev.next
            prev.next = curr
            
            # Move to the next node in the original list
            curr = next_node
            
        return dummy.next