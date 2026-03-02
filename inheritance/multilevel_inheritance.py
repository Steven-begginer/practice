class Grandparent:
    def legacy(self):
        print("Legacy from Grandparent")

class Parent(Grandparent):
    def occupation(self):
        print("Occupation from Parent")

class Child(Parent):
    def hobby(self):
        print("Hobby from Child")

# Child can access: legacy(), occupation(), and hobby()