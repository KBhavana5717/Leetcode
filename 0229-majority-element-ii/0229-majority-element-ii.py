class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
            
        cand1, cand2, count1, count2 = 0, 1, 0, 0
        
        # First pass: find potential candidates
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
                
        # Second pass: verify the candidates
        result = []
        threshold = len(nums) // 3
        
        for cand in set([cand1, cand2]):
            if nums.count(cand) > threshold:
                result.append(cand)
                
        return result