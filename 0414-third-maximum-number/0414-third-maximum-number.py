class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        # Remove duplicates by converting the list to a set
        distinct_nums = set(nums)
        
        # Find the maximum element
        first_max = max(distinct_nums)
        
        # If there are fewer than 3 distinct elements, return the maximum
        if len(distinct_nums) < 3:
            return first_max
        
        # Otherwise, remove the first max and second max to find the third max
        distinct_nums.remove(first_max)
        second_max = max(distinct_nums)
        distinct_nums.remove(second_max)
        
        return max(distinct_nums)