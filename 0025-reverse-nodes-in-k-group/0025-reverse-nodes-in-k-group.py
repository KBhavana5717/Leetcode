# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to check if there are at least k nodes remaining
        def get_kth_node(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # Find the kth node from the current group's previous node
            kth = get_kth_node(group_prev, k)
            if not kth:
                break
                
            group_next = kth.next
            
            # Reverse the k nodes
            prev = kth.next
            curr = group_prev.next
            
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
            # Connect the reversed group back to the rest of the list
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
            
        return dummy.next
        