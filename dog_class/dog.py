# 1. Define the class blueprint
class Dog:
    """A simple class to represent a dog."""
    
    # 2. The __init__ method runs when a new Dog object is made
    def __init__(self, name, breed):
        self.name = name  # Attribute specific to each dog
        self.breed = breed # Attribute specific to each dog
        self.is_sitting = False # Default attribute
    
    # 3. Define methods (behaviors)
    def bark(self):
        """Simulate a dog barking."""
        print(f"{self.name} says WOOF!")
        
    def sit(self):
        """Make the dog sit."""
        if not self.is_sitting:
            self.is_sitting = True
            print(f"{self.name} is now sitting.")
        else:
            print(f"{self.name} is already sitting.")

# 4. Use the class to create objects (instantiation)
# We create two distinct instances of the Dog class:
dog_instance_1 = Dog("Buddy", "Golden Retriever")
dog_instance_2 = Dog("Max", "German Shepherd")

# 5. Access attributes and call methods
print(f"{dog_instance_1.name} is a {dog_instance_1.breed}.")
dog_instance_1.bark() # Output: Buddy says WOOF!

print(f"{dog_instance_2.name} is a {dog_instance_2.breed}.")
dog_instance_2.sit() # Output: Max is now sitting.
dog_instance_2.sit() # Output: Max is already sitting.
