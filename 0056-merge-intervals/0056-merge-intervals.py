class Solution:
    def merge(self, intervals):
        # Step 1: Sort by start time
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            # If merged is empty or no overlap
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # Overlap → merge
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
