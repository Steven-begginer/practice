# we can utilize double underscore to protect the stably internal attributes of specific class.
class Bird:
    def __init__(self):
        self.__type = "Standard Bird" # Mangled to _Bird__type
    
    def show_parent_type(self):
        # This method looks specifically for _Bird__type
        print(f"Parent logic safe: {self.__type}")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        self.__type = "Penguin"# Mangled to _Penguin__type

p = Penguin()
p.show_parent_type()  # Output: Standard Bird (Safe!)
p._Bird__type = "new"
p.show_parent_type()
print(f"Child data: {p._Penguin__type}") # Accessing the child's version
