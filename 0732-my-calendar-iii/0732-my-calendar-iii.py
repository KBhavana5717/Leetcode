from collections import defaultdict

class MyCalendarThree:

    def __init__(self):
        self.timeline = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.timeline[startTime] += 1
        self.timeline[endTime] -= 1
        
        cur = 0
        ans = 0
        for t in sorted(self.timeline):
            cur += self.timeline[t]
            ans = max(ans, cur)
            
        return ans