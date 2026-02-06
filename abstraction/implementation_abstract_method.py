from abstraction1 import Action

class Createstudentsaction(Action): # inherience abstract class: Action
    def execute(self):
        return ("create a new student") # must implement this abstract method.

        