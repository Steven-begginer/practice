class Parent:
    def greet(self, name):
        return f"Hello, {name}"

class Child(Parent):
    def greet(self, name, age):
        # The subclass takes 'name' AND 'age'
        # But it only passes 'name' to the parent because that's all Parent needs
        basic_greeting = super().greet(name) 
        return f"{basic_greeting}, you are {age} years old."
    
child = Child()
print(child.greet("steven", 20))