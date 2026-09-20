class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # If the length of the set is smaller than the list, duplicates exist
        return len(set(nums)) != len(nums)