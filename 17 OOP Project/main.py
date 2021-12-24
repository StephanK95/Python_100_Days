class User:
    def __init__(self, id, username):
        print("new user")
        self.id = id
        self.username = username
        self.followrs = 0
        self.following = 0

    def follow(self, user):
        pass



user_1 = User()
user_1.id = "001"
user_1.username = "angela"

print(user_1.username)

user_2 = User(3, "Stephan")
print(user_2.username)

#Defult values

