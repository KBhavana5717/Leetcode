class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.overlaps:
            if max(startTime, s) < min(endTime, e):
                return False
        
        for s, e in self.booked:
            if max(startTime, s) < min(endTime, e):
                self.overlaps.append((max(startTime, s), min(endTime, e)))
                
        self.booked.append((startTime, endTime))
        return True