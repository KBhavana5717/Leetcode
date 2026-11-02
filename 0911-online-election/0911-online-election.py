from collections import defaultdict
import bisect

class TopVotedCandidate:

    def __init__(self, persons: list[int], times: list[int]):
        self.times = times
        self.leaders = []
        vote_count = defaultdict(int)
        leader = -1
        max_votes = 0
        
        for p in persons:
            vote_count[p] += 1
            if vote_count[p] >= max_votes:
                max_votes = vote_count[p]
                leader = p
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]