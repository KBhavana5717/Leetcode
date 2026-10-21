from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            start = heap[0]                      # smallest remaining card

            # Try to build start, start+1, ..., start+groupSize-1
            for card in range(start, start + groupSize):
                if count[card] == 0:
                    return False
                count[card] -= 1

                if count[card] == 0:
                    # Only the smallest card can be removed from the heap.
                    # If it isn't the smallest, a gap exists, so fail.
                    if card != heap[0]:
                        return False
                    heapq.heappop(heap)

        return True