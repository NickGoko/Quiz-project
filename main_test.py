class Instagram:
    def __init__(self, user_id, username):
        self.user_id = user_id              # Creating attributes what the object has.
        self.username = username
        self.followers = 0
        self.following = 0

    # Method
    def follow(self, user):
        user.followers += 1     # The user/user2 you follow gets one follower
        self.following += 1     # Mean i am/user1 following one more person or rather the object is


user1 = Instagram( "001", "Angela")
user2 = Instagram("002", "Jack")
# print(user1.user_id)
# print(user2.username)

user1.follow(user2)
print(user2.followers)
print(user2.following)
print(user1.followers)
print(user1.following)


