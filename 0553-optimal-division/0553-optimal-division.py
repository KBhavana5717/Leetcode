from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return f"{nums[0]}/{nums[1]}"
        
        # To maximize the division result, we want the numerator to be as large as possible 
        # and the denominator to be as small as possible. 
        # Putting parentheses around all elements starting from the second element 
        # turns the entire remainder into a denominator product, which pulls it up to the numerator.
        
        rest = "/".join(map(str, nums[1:]))
        return f"{nums[0]}/({rest})"