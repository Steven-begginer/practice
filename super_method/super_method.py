class Vehicle:
    def __init__(self, brand, model):
        # Initialize common parameters
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        # 1. Store the extra parameter unique to Car
        self.doors = doors
        
        # 2. Use super() to pass common parameters to the Vehicle class
        super().__init__(brand, model)

# Usage
my_car = Car("Toyota", "Corolla", 4)

print(f"Brand: {my_car.brand}")  # From Parent
print(f"Doors: {my_car.doors}")  # From Subclass
