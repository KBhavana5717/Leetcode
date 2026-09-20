from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)    # userId -> list of (time, tweetId)
        self.following = defaultdict(set)  # userId -> set of followee IDs

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        # Include the user themselves along with all the users they follow
        users = self.following[userId] | {userId}
        min_heap = []
        
        for u in users:
            # Traverse user's tweets from most recent to oldest
            for t in reversed(self.tweets[u]):
                if len(min_heap) < 10:
                    heapq.heappush(min_heap, t)
                else:
                    if t[0] > min_heap[0][0]:
                        heapq.heappushpop(min_heap, t)
                    else:
                        # Since tweets are in chronological order, older tweets can be skipped
                        break
                        
        # Extract the tweets sorted from most recent to least recent
        min_heap.sort(key=lambda x: -x[0])
        return [tweetId for _, tweetId in min_heap]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId, tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId, followeeId)
# obj.unfollow(followerId, followeeId)