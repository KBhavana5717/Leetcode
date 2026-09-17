# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        # Helper counter to break ties in heap when node values are equal
        # (prevents comparison errors between ListNode objects directly)
        
        dummy = ListNode(0)
        current = dummy
        min_heap = []
        
        # Push the first node of each non-empty linked list into the heap
        for i, l in enumerate(lists):
            if l:
                # Store tuple: (node.val, index, node)
                heapq.heappush(min_heap, (l.val, i, l))
                
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            
            # If there is a next node in the same list, push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next
        