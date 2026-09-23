from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert all "HH:MM" timestamps into total minutes from 00:00
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            minutes.append(h * 60 + m)
            
        # Sort the minutes in ascending order
        minutes.sort()
        
        # Initialize minimum difference with the difference between the first and last element 
        # (wrapping around the 24-hour clock: 1440 minutes in a day)
        min_diff = (minutes[0] + 1440) - minutes[-1]
        
        # Check differences between adjacent elements in the sorted list
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
            
        return min_diff