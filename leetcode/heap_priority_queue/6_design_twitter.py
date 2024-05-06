"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
and is able to seethe 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
Each item in the news feed must be posted by users who the user followed or by the user themself.
Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user
with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the
user with ID followeeId.
"""

import heapq
from collections import defaultdict
from typing import DefaultDict, List, Set, Tuple


class Twitter:
    def __init__(self):
        # Initialize the Twitter object
        self.count: int = 0  # Used to assign decreasing timestamps to tweets
        self.tweets: DefaultDict[List[Tuple[int]]] = defaultdict(
            list
        )  # Dictionary to store tweets by user ID
        self.followers: DefaultDict[int, Set] = defaultdict(
            set
        )  # Dictionary to store followers by user ID

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Compose a new tweet with ID tweetId by the user userId
        self.tweets[userId].append(
            (self.count, tweetId)
        )  # Store the tweet with timestamp
        self.count -= 1  # Decrement the count for assigning the next timestamp

    def getNewsFeed(self, userId: int) -> List[int]:
        # Retrieve the 10 most recent tweet IDs in the user's news feed
        res: List[int] = []  # Result list to store the tweet IDs
        min_heap = []  # Min heap to keep track of latest tweets from followed users

        # Include the user's own ID in the followers set
        self.followers[userId].add(userId)

        # Gather latest tweets from users the current user follows
        for followee_id in self.followers[userId]:
            if followee_id in self.tweets:
                # Get the index of the latest tweet from the followee
                index = len(self.tweets[followee_id]) - 1
                # Get the timestamp and tweet ID of the latest tweet
                count, tweet_id = self.tweets[followee_id][index]
                # Push the tweet into the min heap (using negative timestamp for max heap behavior)
                min_heap.append((count, tweet_id, followee_id, index - 1))

        # Heapify the min heap to maintain the latest tweets at the top
        heapq.heapify(min_heap)

        # Retrieve up to 10 most recent tweets from the min heap
        while min_heap and len(res) < 10:
            # Pop the tweet with the latest timestamp from the min heap
            count, tweet_id, followee_id, index = heapq.heappop(min_heap)
            # Append the tweet ID to the result list
            res.append(tweet_id)
            # If there are more tweets from the same followee, push the next tweet into the min heap
            if index >= 0:
                count, tweet_id = self.tweets[followee_id][index]
                heapq.heappush(min_heap, (count, tweet_id, followee_id, index - 1))

        return res  # Return the 10 most recent tweet IDs in the user's news feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # Start following the user with ID followeeId
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Stop following the user with ID followeeId
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Example usage:
if __name__ == "__main__":
    # Create a Twitter object
    twitter: Twitter = Twitter()

    # Post a tweet by user 1
    print(twitter.postTweet(1, 5))

    # Get the news feed of user 1
    print(twitter.getNewsFeed(1))

    # User 1 follows user 2
    print(twitter.follow(1, 2))

    # Post a tweet by user 2
    print(twitter.postTweet(2, 6))

    # Get the updated news feed of user 1
    print(twitter.getNewsFeed(1))

    # User 1 unfollows user 2
    print(twitter.unfollow(1, 2))

    # Get the final news feed of user 1
    print(twitter.getNewsFeed(1))
