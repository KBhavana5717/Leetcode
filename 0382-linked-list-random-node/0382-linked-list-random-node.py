import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        current = self.head
        ans = None
        i = 1
        
        while current:
            # Pick the current node with probability 1/i
            if random.randint(1, i) == 1:
                ans = current.val
            current = current.next
            i += 1
            
        return ans