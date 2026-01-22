class Student:
    def __init__(self, name, house, patronus): #self means executing the current object
        # avoid the incorrect inputs at the start!
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name 
        self.house = house 
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐕"
            case _:
                return "🖊"
            
    #Getter and Setter is for verifying the changed values.
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    #Getter: read and print
    @property
    def house(self):
        return self._house
    #Setter: assign and change the value of the property.
    @house.setter 
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name, house, patronus)
def main():
    student = Student.get()
    print(student.charm())
    # A representation of the *returned value* before it is printed:
"""
<Student object at memory_address_xyz> {
    name: "Harry",
    house: "Gryffindor",
    patronus: "Stag",
    __str__ method: (function pointer),
    charm method: (function pointer)
}
"""
"""
def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)
"""
"""
<Student object at memory_address_xyz> {
    name: "Harry",
    house: "Gryffindor",
    patronus: "Stag",
    __str__ method: (function pointer),
    charm method: (function pointer)
}
"""

if __name__ == "__main__":
    main()