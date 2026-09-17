# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases like removing the head node
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        # Move fast pointer n + 1 steps ahead so that there is a gap of n nodes between slow and fast
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers until fast reaches the end of the list
        while fast:
            slow = slow.next
            fast = fast.next
            
        # Remove the target node by skipping it
        slow.next = slow.next.next
        
        return dummy.next