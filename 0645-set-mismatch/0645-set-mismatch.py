class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))
        
        # Expected sum of numbers from 1 to n
        expected_sum = n * (n + 1) // 2
        
        # Duplicate number is the actual sum minus the sum of unique elements
        duplicate = actual_sum - unique_sum
        
        # Missing number is the expected sum minus the sum of unique elements
        missing = expected_sum - unique_sum
        
        return [duplicate, missing]