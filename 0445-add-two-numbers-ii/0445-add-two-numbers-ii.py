# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        stack1 = []
        stack2 = []
        
        # Push all elements of l1 onto stack1
        curr = l1
        while curr:
            stack1.append(curr.val)
            curr = curr.next
            
        # Push all elements of l2 onto stack2
        curr = l2
        while curr:
            stack2.append(curr.val)
            curr = curr.next
            
        head = None
        carry = 0
        
        # Pop from stacks to add numbers from right to left
        while stack1 or stack2 or carry:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0
            
            total = v1 + v2 + carry
            carry = total // 10
            
            # Create new node and insert it at the beginning of the result list
            new_node = ListNode(total % 10)
            new_node.next = head
            head = new_node
            
        return head