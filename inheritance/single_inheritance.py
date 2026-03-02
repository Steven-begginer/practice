class Parent:
    def feature1(self):
        print("Feature 1 from Parent")

class Child(Parent):
    def feature2(self):
        print("Feature 2 from Child")
print(Child().feature1())
print(Child().feature2())
# Child has access to feature1 and feature2