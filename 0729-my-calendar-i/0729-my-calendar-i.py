class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.calendar:
            if max(start, startTime) < min(end, endTime):
                return False
        self.calendar.append((startTime, endTime))
        return True