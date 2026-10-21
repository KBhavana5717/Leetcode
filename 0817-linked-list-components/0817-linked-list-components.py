class Solution:
    def numComponents(self, head: ListNode | None, nums: list[int]) -> int:
        nums_set = set(nums)
        ans = 0
        curr = head
        in_component = False
        
        while curr:
            if curr.val in nums_set:
                if not in_component:
                    ans += 1
                    in_component = True
            else:
                in_component = False
            curr = curr.next
            
        return ans