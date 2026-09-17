# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        
        curr = head
        while curr:
            # Check if it's the start of a duplicate sequence
            if curr.next and curr.val == curr.next.val:
                # Skip all nodes with the duplicate value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Link prev to the node after the last duplicate
                prev.next = curr.next
            else:
                # No duplicate, move prev forward
                prev = prev.next
                
            curr = curr.next
            
        return dummy.next