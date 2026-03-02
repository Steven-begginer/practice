class Parent:
    def family_name(self):
        print("Smith")

class Daughter1(Parent):
    def profession1(self):
        print("Doctor")

class Daughter2(Parent):
    def profession2(self):
        print("Engineer")

# Daughter1 and Daughter2 both know their family_name, 
# but Daughter1 cannot access profession2.