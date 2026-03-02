class Mother:
    def eye_color(self):
        print("Brown eyes")

class Father:
    def height(self):
        print("Tall")

class Child(Mother, Father):
    pass

# Child has access to BOTH eye_color() and height()