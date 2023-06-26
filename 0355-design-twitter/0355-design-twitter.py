class Twitter:

    def __init__(self):
        self.follows = {} # userId : followings(set)
        self.posts = {} # userId, posts(list)
        self.post_count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append([tweetId, self.post_count])
        self.post_count += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []
        
        if userId in self.follows:
            for followeeId in self.follows[userId]:
                if followeeId in self.posts:
                    posts += self.posts[followeeId]
        
        if userId in self.posts:
            posts += self.posts[userId]
            
        posts.sort(key=lambda x:x[1])
        posts.reverse()
        
        ret = []
        for post in posts:
            ret.append(post[0])
    
            
        return ret[:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
    


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)