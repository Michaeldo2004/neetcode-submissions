import heapq
class Twitter:

    def __init__(self):
        self.followers = {}     # uid: [following]
        self.tweet = {}         # uid: [(action,tweet)]
        self.action = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet.keys():
            self.tweet[userId] = [(self.action, tweetId)]
        else:
            self.tweet[userId].append((self.action, tweetId))
        self.action += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        if userId in self.tweet.keys():
            for act, post in self.tweet.get(userId, []):
                if len(heap) < 10:
                    heapq.heappush(heap, (act, post))
                else:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (act, post))
        if userId in self.followers.keys():
            for user in self.followers[userId]:
                for act, post in self.tweet.get(user, []):
                    if len(heap) < 10:
                        heapq.heappush(heap, (act, post))
                    else:
                        heapq.heappop(heap)
                        heapq.heappush(heap,  (act, post))
        return [item[1] for item in sorted(heap, reverse=True)]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId not in self.followers.keys():
                self.followers[followerId] = [followeeId]
            elif followeeId not in self.followers[followerId]:
                self.followers[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers.keys() and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
