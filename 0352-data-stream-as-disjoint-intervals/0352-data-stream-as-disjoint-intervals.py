class SummaryRanges:

    def __init__(self):
        # We'll store the numbers in a set to avoid duplicates, 
        # and maintain intervals cleanly.
        self.values = set()

    def addNum(self, value: int) -> None:
        self.values.add(value)

    def getIntervals(self) -> list[list[int]]:
        if not self.values:
            return []
            
        # Sort the unique numbers present in the stream
        nums = sorted(list(self.values))
        intervals = []
        
        start = nums[0]
        end = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                # Extend the current interval
                end = nums[i]
            else:
                # Push the completed interval and start a new one
                intervals.append([start, end])
                start = nums[i]
                end = nums[i]
                
        # Append the final interval
        intervals.append([start, end])
        return intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()