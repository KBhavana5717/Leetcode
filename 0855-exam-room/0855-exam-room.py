import bisect

class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.seats = []          # sorted list of occupied seats

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0

        # Candidate 1: seat 0, if it's free. Distance = first occupied seat.
        best_dist = self.seats[0]
        best_seat = 0

        # Candidate 2: the middle of each gap between two students.
        for a, b in zip(self.seats, self.seats[1:]):
            d = (b - a) // 2
            if d > best_dist:          # strict > keeps the lowest seat on ties
                best_dist = d
                best_seat = a + d

        # Candidate 3: the last seat, if it's free.
        if self.n - 1 - self.seats[-1] > best_dist:
            best_seat = self.n - 1

        bisect.insort(self.seats, best_seat)
        return best_seat

    def leave(self, p: int) -> None:
        self.seats.remove(p)