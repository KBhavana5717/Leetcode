class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total_duration = 0
        for i in range(len(timeSeries) - 1):
            # Add the actual duration or the time gap until the next attack, whichever is smaller
            total_duration += min(duration, timeSeries[i + 1] - timeSeries[i])
            
        # Add the full duration for the very last attack
        total_duration += duration
        
        return total_duration