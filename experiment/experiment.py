class User:
    # Class Variable
    active_users_count = 0
    username = "Bob"

    def __init__(self, username):
        # Instance Variable (specific to each user object)
        self.username = username
        User.active_users_count += 1

    # INSTANCE METHOD: This works fine
    def display_username(self):
        # Can access both self.username and self.active_users_count
        return (f"User: {self.username} (Total active: {User.active_users_count})")

    # CLASS METHOD: This will cause an error if used incorrectly
    @classmethod
    def get_user_status_BAD(cls):
        # ERROR: You cannot use 'self' here. 'cls' is passed instead.
        return f"Status for: {cls.active_users_count}" 

# Create an instance
user1 = User("Alice")
print(user1.active_users_count)
user2 = User("Bob")
print(user2.active_users_count)
# Both calls would crash because 'cls' (the User class) has no 'username'
# The error message would look something like this:
# AttributeError: type object 'User' has no attribute 'username'
