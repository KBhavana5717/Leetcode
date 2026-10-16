class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Find the total length of the linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        # Step 2: Determine the size of each part
        base_size = length // k
        remainder = length % k
        
        res = []
        curr = head
        
        # Step 3: Split the list into k parts
        for i in range(k):
            res.append(curr)
            part_size = base_size + (1 if i < remainder else 0)
            
            # Traverse to the end of the current part
            tail = None
            for _ in range(part_size):
                if curr:
                    tail = curr
                    curr = curr.next
                    
            # Cut the connection to form a separate part
            if tail:
                tail.next = None
                
        return res