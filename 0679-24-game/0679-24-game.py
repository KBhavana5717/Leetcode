class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        def solve(nums):
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        
                        a, b = nums[i], nums[j]
                        
                        res = [a + b, a * b, a - b, b - a]
                        if abs(b) > 1e-6:
                            res.append(a / b)
                        if abs(a) > 1e-6:
                            res.append(b / a)
                            
                        for val in res:
                            if solve(next_nums + [val]):
                                return True
            return False

        return solve([float(c) for c in cards])