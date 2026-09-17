# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases easily
        dummy = ListNode(0, head)
        current = dummy
        
        # Iterate as long as there are at least two nodes left to swap
        while current.next and current.next.next:
            # Identify the two nodes to swap
            first = current.next
            second = current.next.next
            
            # Perform the swap
            first.next = second.next
            second.next = first
            current.next = second
            
            # Move the pointer two nodes forward for the next pair
            current = first
            
        return dummy.next
        