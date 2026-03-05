class MyClass():

    #a class variable that will list all instances
    instances = []

    def __init__(self, name: str):
        #initialise this instance normally
        self.name = name

        #add this instance to the class instances
        MyClass.instances.append(self)

#we create some instances
MyClass("Never")
MyClass("Gonna")
MyClass("Give")
MyClass("You")
MyClass("Up")
#note how we have no local variable to access these instances.
#we can access these instances via the class(it is like store the instance like dictionary "name" : "never"
for instance in MyClass.instances:
    print(instance.name)