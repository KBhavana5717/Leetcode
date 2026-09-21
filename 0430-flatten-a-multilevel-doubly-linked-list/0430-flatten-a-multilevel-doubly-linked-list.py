class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head
        while curr:
            if curr.child:
                # Save the next node
                next_node = curr.next
                
                # Connect curr to its child
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
                
                # Find the tail of the child list
                tail = curr.next
                while tail.next:
                    tail = tail.next
                
                # Reconnect the tail to the saved next_node, if it exists
                if next_node:
                    tail.next = next_node
                    next_node.prev = tail
            
            curr = curr.next
            
        return head