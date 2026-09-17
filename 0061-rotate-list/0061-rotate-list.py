# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Base cases: if the list is empty, has only one node, or k is 0
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length of the linked list and locate the tail node
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Connect the tail to the head to form a circular linked list
        tail.next = head
        
        # Step 3: Find the effective rotations needed
        k = k % length
        if k == 0:
            tail.next = None
            return head
        
        # Step 4: Find the new tail and new head
        # The new tail will be at position (length - k - 1) from the start
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        
        # Step 5: Break the circle
        new_tail.next = None
        
        return new_head