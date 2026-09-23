class Solution:
    def checkRecord(self, s: str) -> bool:
        # Check if the total number of 'A' (absent) is strictly fewer than 2,
        # and check if 'LLL' (3 or more consecutive late days) is not in the string.
        return s.count('A') < 2 and 'LLL' not in s