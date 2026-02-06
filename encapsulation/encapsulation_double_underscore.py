class User:
    def __init__(self, username):
        self.__username = username  # Protected (internal) by convention

    @property
    def username(self):
        return self.__username.upper() # Logic inside the getter

    @username.setter
    def username(self, value):
        if len(value) < 3:
            raise ValueError("Username too short!")
        self.__username = value

    def __str__(self):
        return self.__username
    
user1 = User("nabi")
print(user1)
user1.__username = "xiaojiujiu"
print(user1)

#I use the double underscore to avoid the subclasses(parent class and child class).